#!/usr/bin/python
import urllib2

class LettoreFile:
    input = ""
    output = ""

    def __init__(self, i, o):
        self.input = open(i, 'r')
        self.output = open(o, 'w')

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
            splitted = line.split()
            for word in splitted:
                if word in mappa:
                    mappa[word] = (mappa[word][0] + 1, mappa[word][1] + 1)
                else:
                    mappa[word] = (1, 1)

        for keyword in mappa.keys():
            if keyword in self.dizionario:
                self.dizionario[keyword] = (self.dizionario[word][0] + 1, self.dizionario[word][1] + 1)
            else:
                self.dizionario[keyword] = (1, 1)

    def printer(self):
        f = open('dizout.txt', 'w')
        for x in self.dizionario:
            f.write(str(self.dizionario[x][0]))
            f.write(" ")
            f.write(str(self.dizionario[x][1]))
            f.write(' ')
            f.write(x)
            f.write('\n')
        f.close()

def main():
    page1 = urllib2.urlopen('http://www.unive.it/data/46/1')
    page2 = urllib2.urlopen('http://www.unive.it/data/46/2')
    page3 = urllib2.urlopen('http://www.unive.it/data/46/3')
    output1 = open('output1.txt', 'w')
    output2 = open('output2.txt', 'w')
    output3 = open('output3.txt', 'w')

    for line in page1:
        output1.write(line)

    for line in page2:
        output2.write(line)

    for line in page3:
        output3.write(line)

    output1.close()
    output2.close()
    output3.close()

    lista=('output1.txt','output2.txt','output3.txt')

    Variabile=GestoreCollezioneFile(lista)
    Variabile.printer()

#Esecutore intero progetto
if __name__ == "__main__":
    main()