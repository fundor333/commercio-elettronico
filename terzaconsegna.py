import re

from bson import Code
import numpy
from numpy.ma import sqrt
import pymongo

from userclass import User


__author__ = 'Fundor333'

import linecache

from mongodbclass import database
from primaconsegna import getfromgoogle, NUMERORISULTATI, OUTPITFILENAME


INSERITO = 1
NAMEDB = "Silvestri"
DBM = database(NAMEDB, 'localhost', 27017)
DOCUMENTCOLLECTION = "documenti"
LEXICONNAME = "lexicon.txt"
LEXICON = []
USERCOLLECTION = "user"
DOCUMENTLIST = {"./out/7.txt", "./out/6.txt", "./out/5.txt", "./out/4.txt", "./out/3.txt", "./out/2.txt",
                "./out/1.txt", "./out/0.txt"}



def readlexicon():
    lexiconnum = 0
    lexicondict = {}
    filein = open(LEXICONNAME)
    for word in filein:
        if word != "" and word != "\n":
            lexicondict[word.replace("\n", "")] = lexiconnum
            lexiconnum += 1
    return lexicondict, lexiconnum


def elaboratoretesti(texts, namefile):
    jsoonvar = {"_id": namefile, "body": texts}
    return jsoonvar


def recuperodocumenti():
    try:
        open("./out/" + OUTPITFILENAME + ".txt")
        num = linecache.getline("./out/" + OUTPITFILENAME + ".txt", 1)
        print("Ho recuperato i documenti")

    except IOError:
        num = getfromgoogle(NUMERORISULTATI)
        print("Ho generato i documenti")

    if INSERITO == 0:
        print("Ecco gli ID dei documenti")
        print("##############")

        for i in range(0, int(num)):
            textappend = ""
            fileinname = "./out/" + str(i) + ".txt"
            filein = open(fileinname)
            for line in filein:
                textappend += line
            print(DBM.insert(DOCUMENTCOLLECTION, elaboratoretesti(textappend, fileinname)))

        print("##############")
        print("Fine degli ID nei documenti")
    return num


def elaborodocumenti():
    print("Elaboro i dati")
    mapper = Code(open('mapper.js', 'r').read())
    reducer = Code(open('reducer.js', 'r').read())
    reduction = DBM.mapreducer(mapper, reducer, "risultati", DOCUMENTCOLLECTION)
    print("Frequenza delle parole")
    fileout = open("terzaout.txt", 'w')
    outlexicon = open(LEXICONNAME, 'w')
    for element in reduction.find():
        fileout.write(str(element['_id']) + " " + str(element['value']) + '\n')
        LEXICON.append(str(element['_id']))
        outlexicon.write(str(element['_id']) + '\n')
    fileout.close()
    outlexicon.close()
    outfile = open("parolepiufrequenti.txt", 'w')
    for line in reduction.find().sort("value", pymongo.DESCENDING).limit(20):
        outfile.write(line['_id'] + "\n")
    outfile.close()


def coscalc(arr1, arr2):
    x = 0
    y = 0
    xy = 0
    for num in range(0, arr1.size - 1):
        x += arr1[num] * arr1[num]
        y += arr2[num] * arr2[num]
        xy += arr1[num] * arr2[num]
    y = sqrt(y)
    x = sqrt(x)
    cosenocal = 1 - (xy / (x * y))
    return cosenocal


def readerpage(inputfile, lexicon, numword):
    arraydictionary = range(0, numword)
    for parts in inputfile.split():
        for word in re.split("[^a-zA-Z]", parts):
            if word != '' and word != "u":
                arraydictionary[lexicon[word.lower()]] += 1
    return numpy.array(arraydictionary)


def partenza(numerodoc, utente):
    lexicon, numword = readlexicon()
    fileout = open("similitudiniterza.txt", 'w')
    contenitore_nome_testi = utente.getjson()["text"]
    filebody = ""
    for text in contenitore_nome_testi:
        filebody += DBM.returntext(DOCUMENTCOLLECTION, text)["body"]
    arr1 = readerpage(filebody, lexicon, numword)
    arrayslist = {}
    for i in range(1, int(numerodoc)):
        filename = "./out/" + str(i) + ".txt"
        filebody = DBM.returntext(DOCUMENTCOLLECTION, filename)["body"]
        arr2 = readerpage(filebody, lexicon, numword)
        arrayslist[str(coscalc(arr1, arr2))] = filename
    listcold = arrayslist.keys()
    listcold.sort()
    for i in range(len(arrayslist) - 9, len(arrayslist)):
        fileout.write(arrayslist[listcold[i]] + '\n')
    fileout.close()


def main():
    numerodoc = recuperodocumenti()
    elaborodocumenti()
    utente = User(DOCUMENTLIST, LEXICON, "utente")
    if INSERITO == 0:
        DBM.insert(USERCOLLECTION, utente.getjson())
    partenza(numerodoc, utente)


if __name__ == "__main__":
    main()