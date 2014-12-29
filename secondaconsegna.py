__author__ = 'Fundor333'

import codecs
import re

import numpy
from numpy.ma import sqrt

from primaconsegna import getfromgoogle, NUMERORISULTATI


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


def printlexicon(lexicon):
    fileout = codecs.open("./out/lexicon.txt", 'w', 'utf-8')
    appoggio = ["" for _ in lexicon[1].items()]
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
    lexicon_num = 0
    lexicon_dict = {}
    filein = open(LEXICONNAME)
    num_line = 0
    i = 0
    for line in filein:
        if i == 0:
            i += 1
            num_line = line
        else:
            word, m, n = line.split()
            lexicon_dict[word] = lexicon_num
            lexicon_num = lexicon_num + 1
    return lexicon_num, lexicon_dict, num_line


def returnsimilar(interestingarray, arrayslist):  # arraylist[i][0]=nomefile,arraylist[i][1]=array del file
    similardictionary = {}
    for name in arrayslist:
        similardictionary[coscalc(interestingarray, name[1])] = name[0]
    fileout = open(LEXICONNAME, 'w')
    listsorted = similardictionary.keys()
    listsorted.sort()
    for i in range(len(listsorted) - 9, len(listsorted)):
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


def main():
    appoggio = []
    lexicon = (0, {})
    try:
        lexicon_num, lexicondict, numero_file = readlexicon()
        lexicon = (lexicon_num, lexicondict)
        printlexicon(lexicon)
    except Exception:
        numero_file = getfromgoogle(NUMERORISULTATI)
        for i in range(0, numero_file):
            inputfile = "./out/" + str(i) + ".txt"
            lexicon_num, lexicondict, = addtolexicon(lexicon, inputfile)
            lexicon = (lexicon_num, lexicondict)
            appoggio.append(inputfile)
        printlexicon(lexicon)


    # Partenza a freddo
    print("Cold start")
    singlefile = "./out/0.txt"
    fileout = open("./out/coldstart.txt", 'w')
    arrayslist_cold = {}
    arr1 = readerpage(singlefile, lexicon)
    for i in range(1, int(numero_file)):
        tempfilename = "./out/" + str(i) + ".txt"
        arr2 = readerpage(tempfilename, lexicon)
        arrayslist_cold[str(coscalc(arr1, arr2))] = tempfilename
    listcold = arrayslist_cold.keys()
    listcold.sort()
    for i in range(len(arrayslist_cold) - 9, len(arrayslist_cold)):
        fileout.write(arrayslist_cold[listcold[i]] + '\n')
    fileout.close()

    # Partenza a caldo
    print("Warm start")
    mydocument = readerpage("./out/0.txt", lexicon)
    for i in range(19, 40):
        filein = "./out/" + str(i) + ".txt"
        mydocument = sumarray(mydocument, readerpage(filein, lexicon))
    arrayslisthot = []
    for i in range(6, int(numero_file)):
        filename = "./out/" + str(i) + ".txt"
        arrayslisthot.append((filename, readerpage(filename, lexicon)))
    returnsimilar(mydocument, arrayslisthot)


# Esecutore intero progetto
if __name__ == "__main__":
    main()