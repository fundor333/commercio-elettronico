from math import sqrt
import re

__author__ = 'Fundor333'
DIZIONARIOTOTALE = {}

URLFILE = "url.txt"
LEXICONNAME = "lexicon"
USERARRAYNAME = "userarrayname"

# Calcola la distanza tra i due dizionari


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


def userarray(listafiles, lexicon):
    arrayout = []
    for _ in [1, lexicon.lastnumber]:
        arrayout.append(0)
    for filess in listafiles:
        for lines in filess:
            for word in lines:
                arrayout[lexicon.getnumberword(word)] += 1

    fileout = open(USERARRAYNAME, "w")
    for element in arrayout:
        fileout.write(str(element)+'\n')
    fileout.close()


class Lexicon:
    def __init__(self):
        pass

    lastnumber = 0
    dictionaryWord = {}

    def getprintlexicon(self):
        fileout = open(LEXICONNAME, "w")
        appoggio = []
        for _ in[0,self.dictionaryWord.items().__sizeof__()]:
            appoggio.append(0)
        i=0
        for word, number in self.dictionaryWord.items():
            appoggio[number]=word

        for word in appoggio:
            fileout.write(word + " " + str(i) + '\n')
            i+=1
        fileout.close()


    def adddocument(self, filename):
        fileopened = open(filename)
        for line in fileopened:
            for splitted in line.split():
                for word in re.split("[^a-zA-Z]", splitted):
                    if (word != '' or word != ' '):
                        if self.dictionaryWord.keys().__contains__(word.lower()) != 1:
                            self.dictionaryWord[word.lower()] = self.lastnumber
                            self.lastnumber += 1


def main():
    listurl = open(URLFILE)
    i = 0
    lexicon = Lexicon()
    for _ in listurl:
        inputfile = "risultati_" + str(i) + "_changed.txt"
        lexicon.adddocument(inputfile)
        i += 1
    lexicon.getprintlexicon()
    appoggio = []
    for i in [1, 32]:
        inputfile = open("risultati_" + str(i) + "_changed.txt")
        appoggio.append(inputfile)

    userarray(appoggio, lexicon)

# Esecutore intero progetto
if __name__ == "__main__":
    main()