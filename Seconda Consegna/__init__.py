from math import sqrt
import re

__author__ = 'Fundor333'

DIZIONARIOTOTALE = {}
NUM = 665
ELENCOFILE = range(NUM)


class confrontaarray:
    dizionario1 = ""
    dizionario2 = ""
    x = 0
    y = 0
    xy = 0

    def __init__(self, nomefile1, nomefile2):
        self.dizionario1 = DIZIONARIOTOTALE[nomefile1]
        self.dizionario2 = DIZIONARIOTOTALE[nomefile2]
        self.calcolacoseno()

    def calcolacoseno(self):
        for singolakey in self.dizionario1.keys():
            self.x = self.x + self.dizionario1[singolakey]* self.dizionario1[singolakey]
            if singolakey in self.dizionario2.keys():
                self.xy = self.xy + self.dizionario1[singolakey]*self.dizionario2[singolakey]
        for singolakey in self.dizionario2.keys():
            self.y = self.y + self.dizionario2[singolakey]* self.dizionario2[singolakey]
        self.x = sqrt(self.x)
        self.y = sqrt(self.y)
        coseno = (self.xy)/(self.x * self.y)
        print(coseno)
        return coseno


class Lettorefile:
    listanomefile = []

    def __init__(self, listafile):
        self.listanomefile = listafile
        for singolofile in listafile:
            self.readerpage(singolofile)

    def readerpage(self, nomefile):
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


def main():
    for i in range(0, NUM):
        ELENCOFILE[i] = "risultati_" + str(i) + "_changed.txt"

    Lettorefile(ELENCOFILE)
    confrontaarray("risultati_5_changed.txt","risultati_10_changed.txt")

# Esecutore intero progetto
if __name__ == "__main__":
    main()