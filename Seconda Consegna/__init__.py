from math import sqrt
import re

__author__ = 'Fundor333'
DIZIONARIOTOTALE = {}

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
        DIZIONARIOTOTALE[nomefile] = dictionary

def userarray(listafiles):
    pass


class Lexicon:
    def __init__(self):
        pass

    lastnumber = 0
    dictionaryWord = {}

    def adddocument(self, filename):
        fileopened = open(filename)
        for line in fileopened:
            for word in line:
                if self.dictionaryWord[word] != 0:
                    self.dictionaryWord[word] = self.lastnumber
                    self.lastnumber += 1

    def getnumberword(self, word):
        return self.dictionaryWord[word]


def main():
    pass

# Esecutore intero progetto
if __name__ == "__main__":
    main()