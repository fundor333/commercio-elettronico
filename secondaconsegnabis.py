import codecs
import re

__author__ = 'Fundor333'

from primaconsegna import getfromgoogle, NUMERORISULTATI

DIZIONARIOTOTALE = {}
LEXICONNAME = "./out/out.txt"
USERARRAYNAME = "userarrayname"


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

# Esecutore intero progetto


if __name__ == "__main__":
    numerofline = 0
    appoggio = []
    lexicon = (0, {})
    try:
        lexiconnum, lexicondict, numerofline = readlexicon()
        lexicon = (lexiconnum, lexicondict)
        print("Reading the Lexicon")
    except IOError:
        numerofline = getfromgoogle(NUMERORISULTATI)
        print("Generating the Lexicon")
        for i in range(0, numerofline):
            inputfile = "./out/" + str(i) + ".txt"
            lexicon = addtolexicon(lexicon, inputfile)
            appoggio.append(inputfile)
        printlexicon(lexicon)


    # Partenza a freddo
    print("Cold start")

    # Partenza a caldo
    print("Hot start")