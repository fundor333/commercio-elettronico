__author__ = 'Fundor333'

import codecs
import re

from scipy.spatial.distance import cosine
import numpy

from primaconsegna import getfromgoogle, NUMERORISULTATI


DIZIONARIOTOTALE = {}
LEXICONNAME = "./out/out.txt"
USERARRAYNAME = "userarrayname"

# Calcola la distanza tra i due dizionari


def addtolexicon(lexicon, filename):
    lexiconnum = lexicon[0]
    lexicondict = lexicon[1]
    fileopened = open(filename)
    for line in fileopened:
        for splitted in line.split():
            for word in re.split('[^a-zA-Z]', splitted):
                if word != '' or word != ' ':
                    if lexicondict.keys().__contains__(word.lower()) != 1:
                        lexicondict[word.lower()] = lexiconnum
                        lexiconnum += 1
    return (lexiconnum, lexicondict)


# TODO da modificare e correggere
# Non funziona
def coscalc(arr1, arr2):
    return cosine(arr1, arr2)


def printlexicon(lexicon):
    fileout = codecs.open("./out/lexicon.txt", 'w', 'utf-8')
    appoggio = ["" for word, number in lexicon[1].items()]
    for word, number in lexicon[1].items():
        appoggio[number] = word
    i = 1
    for word in appoggio:
        fileout.write(word + " " + str(i) + '\n')
        i += 1
    fileout.close()


def readerpage(file, lexicon):
    listanomefile = ""
    arraydictionary = []
    numword = lexicon[0]
    inputfile = open(file)
    for line in inputfile:
        listanomefile += line
    for i in range(0, numword):
        arraydictionary.append(0)
    for wordss in listanomefile.split():
        for word in re.split("[^a-zA-Z]", wordss):
            if word != '':
                arraydictionary[lexicon[1][word.lower()]] += 1
    return numpy.array(arraydictionary)


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
            word, m, n = line.split()
            lexicondict[word] = lexiconnum
            lexiconnum = lexiconnum + 1
    return lexiconnum, lexicondict, numline


def returnsimilar(interestingarray, arrayslist):  # arraylist[i][0]=nomefile,arraylist[i][1]=array del file
    similardictionary = {}
    for name in arrayslist:
        similardictionary[coscalc(interestingarray, name[1])] = name[0]
    listsorted = sorted(similardictionary, key=lambda key: similardictionary[key])
    fileout = open("./out/hotstart.txt", 'w')
    for i in range(0, 9):
        fileout.write(similardictionary[listsorted[i]] + '\n')
    fileout.close()


def sumarray(arra1, arra2):
    array1 = numpy.array(arra1)
    array2 = numpy.array(arra2)
    return array1 + array2


def userarray(listafiles, lexicon):
    arrayout = []
    for _ in [1, lexicon[0]]:
        arrayout.append(0)
    for filess in listafiles:
        for lines in filess:
            for splitted in lines:
                for word in re.split("[^a-zA-Z]", splitted):
                    if word != '':
                        arrayout[lexicon.getnumberword(word)] += 1

    fileout = open(USERARRAYNAME, "w")
    for element in arrayout:
        fileout.write(str(element) + '\n')
    fileout.close()


# Esecutore intero progetto
if __name__ == "__main__":
    numerofline = 0
    appoggio = []
    lexicon = (0, {})
    try:
        lexiconnum, lexicondict, numerofline = readlexicon()
        lexicon = (lexiconnum, lexicondict)
    except IOError:
        numerofline = getfromgoogle(NUMERORISULTATI)
        for i in range(0, numerofline):
            inputfile = "./out/" + str(i) + ".txt"
            lexicon = addtolexicon(lexicon, inputfile)
            appoggio.append(inputfile)
        printlexicon(lexicon)

    # Partenza a freddo
    print("Cold start")
    singlefile = "./out/0.txt"
    fileout = open("./out/coldstart.txt", 'w')
    arrayslistcold = {}
    arr1 = readerpage(singlefile, lexicon)
    for i in range(1, int(numerofline)):
        tempfilename = "./out/" + str(i) + ".txt"
        arr2 = readerpage(tempfilename, lexicon)
        arrayslistcold[coscalc(arr1, arr2)] = tempfilename
    listsorted = sorted(arrayslistcold, key=lambda key: arrayslistcold[key])
    for i in range(0, 9):
        fileout.write(arrayslistcold[listsorted[i]] + '\n')
    fileout.close()

    # Partenza a caldo
    print("Hot start")
    mydocument = readerpage("./out/0.txt", lexicon)
    for i in range(0, 5):
        filein = "./out/" + str(i) + ".txt"
        mydocument = sumarray(mydocument, readerpage(filein, lexicon))
    arrayslisthot = []
    for i in range(6, int(numerofline)):
        filename = "./out/" + str(i) + ".txt"
        arrayslisthot.append((filename, readerpage(filename, lexicon)))
    returnsimilar(mydocument, arrayslisthot)