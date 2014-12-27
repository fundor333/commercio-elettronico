import re

from bson import Code
import numpy
from numpy.ma import sqrt
import pymongo

from userterzaconsegna import User


__author__ = 'Fundor333'

import linecache

from DatabaseMongoClass import database
from primaconsegna import getfromgoogle, NUMERORISULTATI, OUTPITFILENAME


INSERITO = 1
NAMEDB = "Silvestri"
DBM = database(NAMEDB, 'localhost', 27017)
COLLECTIONNAME = "documenti"
LEXICONNAME = "lexicon.txt"
LEXICON = []


def readlexicon():
    lexiconnum = 0
    lexicondict = {}
    filein = open(LEXICONNAME)
    numline = 0
    i = 0
    for line in filein:
        if i == 0:
            i += 1
            numline = line
        else:
            word = line.split()
            for singe in word:
                lexicondict[singe] = lexiconnum
                lexiconnum = lexiconnum + 1
    return lexiconnum, lexicondict, numline

def elaboratoretesti(texts, namefile):
    jsoonvar = {"_id": namefile, "body": texts}
    return jsoonvar


def recuperodocumenti():
    try:
        open("./out/" + OUTPITFILENAME + ".txt")
        fistline = linecache.getline("./out/" + OUTPITFILENAME + ".txt", 1)
        print("Ho recuperato i documenti")

    except IOError:
        fistline = getfromgoogle(NUMERORISULTATI)
        print("Ho generato i documenti")

    if INSERITO == 0:
        print("Ecco gli ID dei documenti")
        print("##############")

        for i in range(0, int(fistline)):
            textappend = ""
            fileinname = "./out/" + str(i) + ".txt"
            filein = open(fileinname)
            for line in filein:
                textappend += line

        print("##############")
        print("Fine degli ID nei documenti")


def elaborodocumenti():
    print("Elaboro i dati")
    mapper = Code(open('mapper.js', 'r').read())
    reducer = Code(open('reducer.js', 'r').read())
    reduction = DBM.mapreducer(mapper, reducer, "risultati", COLLECTIONNAME)
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


def readerpage(inputfile, lexicon):
    listanomefile = ""
    arraydictionary = []
    for parts in listanomefile.split():
        for word in re.split("[^a-zA-Z]", parts):
            if word != '':
                arraydictionary[lexicon[1][word.lower()]] += 1
    return numpy.array(arraydictionary)


def partenza():
    numerofline = 0
    lexicon = readlexicon()
    singlefile = DBM.returntext(COLLECTIONNAME, "./out/0.txt")["body"]
    fileout = open("start.txt", 'w')
    arrayslist = {}
    arr1 = readerpage(singlefile, lexicon)
    for i in range(1, int(numerofline)):
        tempfilename = DBM.returntext(COLLECTIONNAME, "./out/" + str(i) + ".txt")["body"]
        arr2 = readerpage(tempfilename, lexicon)
        arrayslist[str(coscalc(arr1, arr2))] = tempfilename
    listcold = arrayslist.keys()
    listcold.sort()
    for i in range(len(arrayslist) - 9, len(arrayslist)):
        fileout.write(arrayslist[listcold[i]] + '\n')
    fileout.close()


def main():
    recuperodocumenti()
    elaborodocumenti()
    documentlist = {"./out/7.txt", "./out/6.txt", "./out/5.txt", "./out/4.txt", "./out/3.txt", "./out/2.txt",
                    "./out/1.txt", "./out/0.txt"}
    if INSERITO == 0:
        utente = User(documentlist, LEXICON, "utente")
        DBM.insert("user", utente.getjson())
        # partenza()

if __name__ == "__main__":
    main()