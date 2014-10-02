#!/usr/bin/python

class lettoreFile:
    input = ""
    output = ""

    def __init__(self, i, o):
        self.input = open(i, 'r')
        self.output = open(o, 'w')

    def __init__(self, i):
        self.input = open(i, 'r')

    def tuttomaiuscolo(self):
        for line in input:
            self.output.write(line.upper())

    def chiudi(self):
        self.input.close()
        self.output.close()


class GestoreCollezioneFile:
    listafiletot = None
    dizionario = {}

    def __init__(self, listafile):
        self.listafiletot = listafile
        for file in listafile:
            self.aggiorna(open(file,'r'))

    def aggiorna(self, nomeFile):
        lines = nomeFile.readlines()
        mappa = {}

        for line in lines:
            splitted=line.split()
            for word in splitted:
                if word in mappa:
                    mappa[word]=((mappa[word][0]+1, mappa[word][1]+1))
                else:
                    mappa[word]=(1,1)

        for keyword in mappa.keys():
            if keyword in self.dizionario:
                self.dizionario[keyword]=((self.dizionario[word][0]+1, self.dizionario[word][1]+1))
            else:
                self.dizionario[keyword]=(1,1)

    def printer(self):
        print(self.dizionario)