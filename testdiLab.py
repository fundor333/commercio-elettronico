#!/usr/bin/python
import urllib2


class LettoreFile:
    input = ""
    output = ""

    def __init__(self, i, o):
        self.input = urllib2.urlopen(i)
        self.output = open(o, 'w')

    def elaboratore(self):
        for line in self.input:
            self.output = self.output + self.pulisciparola(line)
        return self

    def pulisciparola(self,word):
        #word= word.split('\W')
        return word

    def tuttomaiuscolo(self):
        for line in self.input:
            self.output.write(line.upper())

    def chiudi(self):
        self.input.close()
        self.output.close()


class GestoreCollezioneFile:
    listafiletot = None
    dizionario = {}

    def __init__(self, listafile):
        self.listafiletot = listafile
        for singlefile in listafile:
            self.aggiorna(open(singlefile, 'r'))

    def aggiorna(self, nomefile):
        lines = nomefile.readlines()
        mappa = {}

        for line in lines:
            splitted = line.upper()
            splitted = splitted.split()
            for word in splitted:
                if word in mappa:
                    mappa[word] = (mappa[word][0] + 1, mappa[word][1] + 1)
                else:
                    mappa[word] = (1, 1)

        for keyword in mappa.keys():
            if keyword in self.dizionario:
                self.dizionario[keyword] = (self.dizionario[keyword][0] + 1, self.dizionario[keyword][1] + 1)
            else:
                self.dizionario[keyword] = (1, 1)

    def printer(self):
        f = open('dizout.txt', 'w')
        for x in self.dizionario:
            f.write(str(self.dizionario[x][0])+" "+str(self.dizionario[x][1])+' '+x+'\n')
        f.close()


def main():
    lista = ('output1.txt', 'output2.txt', 'output3.txt')

    LettoreFile('http://www.unive.it/data/46/1', lista[0])
    LettoreFile('http://www.unive.it/data/46/2', lista[1])
    LettoreFile('http://www.unive.it/data/46/3', lista[2])

    GestoreCollezioneFile(lista).printer()

# Esecutore intero progetto
if __name__ == "__main__":
    main()