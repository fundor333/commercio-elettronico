import codecs
from math import sqrt
import re

from primaconsegna import getfromgoogle, NUMERORISULTATI, getsingledict


__author__ = 'Fundor333'
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


def coscalc(dizionario1, dizionario2):
    x = 0
    y = 0
    xy = 0
    for singolakey in dizionario1.keys():
        x = x + dizionario1[singolakey] * dizionario1[singolakey]
        if singolakey in dizionario2.keys():
            xy = xy + dizionario1[singolakey] * dizionario2[singolakey]
    for singolakey in dizionario2.keys():
        y = y + dizionario2[singolakey] * dizionario2[singolakey]
    x = sqrt(x)
    y = sqrt(y)
    try:
        coseno = xy / (x * y)
    except ZeroDivisionError:
        coseno = 0
    return coseno


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


def readerpage(listanomefile):
    dizionario = {}
    for nomefile in listanomefile:
        singlefile = open(nomefile, 'r')
        dictionary = {}
        for line in singlefile:
            for parolanonelaborata in line.split():
                for singolaparola in re.split("[^a-zA-Z]", parolanonelaborata):
                    if singolaparola != "":
                        if singolaparola in dictionary.keys():
                            dictionary[singolaparola.lower()] += 1
                        else:
                            dictionary[singolaparola.lower()] = 1
        dizionario[nomefile] = dictionary
    return dizionario


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


def openfile(file):
    stringout = ""
    for line in file:
        stringout += line
    return stringout

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
    singlefile = "./out/0.txt"
    fileout = open("./out/singlefile.txt", 'w')
    for i in range(1, int(numerofline)):
        print("Cosin 0.txt with " + str(i) + ".txt")
        tempfilename = "./out/" + str(i) + ".txt"
        tempfilein = open(tempfilename)
        if coscalc(getsingledict(openfile(singlefile)), getsingledict(openfile(tempfilein))) < 0.000000000000001:
            fileout.write(tempfilename + '\n')
    fileout.close()