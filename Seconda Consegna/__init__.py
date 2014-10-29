from math import sqrt
import re

__author__ = 'Fundor333'

DIZIONARIOTOTALE = {}
NUM = 665
ELENCOFILE = range(NUM)


class Confrontaarray:
    dizionario1 = ""
    dizionario2 = ""
    x = 0
    y = 0
    xy = 0

    def __init__(self, nomefile1, nomefile2):
        self.dizionario1 = DIZIONARIOTOTALE[nomefile1]
        self.dizionario2 = DIZIONARIOTOTALE[nomefile2]

    def calcolacoseno(self):
        for singolakey in self.dizionario1.keys():
            self.x = self.x + self.dizionario1[singolakey] * self.dizionario1[singolakey]
            if singolakey in self.dizionario2.keys():
                self.xy = self.xy + self.dizionario1[singolakey] * self.dizionario2[singolakey]
        for singolakey in self.dizionario2.keys():
            self.y = self.y + self.dizionario2[singolakey] * self.dizionario2[singolakey]
        self.x = sqrt(self.x)
        self.y = sqrt(self.y)
        try:
            coseno = self.xy / (self.x * self.y)
        except ZeroDivisionError:
            coseno = 0
        return coseno


class Lettorefile:
    listanomefile = []

    def __init__(self, listafile):
        self.listanomefile = listafile
        self.readerpage()

    def readerpage(self):
        for nomefile in self.listanomefile:
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
    file_out = open("output.txt", 'w')

    for i in range(0, len(ELENCOFILE)):
        print("Giro numero " + str(i) + " su " + str(NUM))
        for y in range(i + 1, len(ELENCOFILE)):
            numero = Confrontaarray("risultati_" + str(i) + "_changed.txt",
                                    "risultati_" + str(y) + "_changed.txt").calcolacoseno()
            file_out.write(str(numero) + "\n")

    file_out.close()

# Esecutore intero progetto
if __name__ == "__main__":
    main()