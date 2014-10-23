import re

__author__ = 'Fundor333'

DIZIONARIOTOTALE = {}
NUM = 665
ELENCOFILE = range(NUM)


class confrontaarray:
    nomefile1 = ""
    nomefile2 = ""

    def __init__(self, nomefile1, nomefile2):
        self.nomefile1 = nomefile1
        self.nomefile2 = nomefile2


class Lettorefile:
    listanomefile = []

    def __init__(self, listafile):
        self.listanomefile = listafile
        for singolofile in listafile:
            self.readerpage(singolofile)
        print(DIZIONARIOTOTALE)

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

# Esecutore intero progetto
if __name__ == "__main__":
    main()