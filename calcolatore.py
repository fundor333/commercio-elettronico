__author__ = 'Fundor333'

import operator

class Contaparole:
    nome = ""
    fileinput = None
    main_dict = {}

    def __init__(self, nome):
        self.nome = nome
        self.fileinput = open(nome, 'r')
        for line in self.fileinput:
            self.appoggiodict(line)

    def appoggiodict(self, rigadelfile):
        new_dict = {}
        rigadelfile = rigadelfile.split()

        for singolaparola in rigadelfile:
            if singolaparola in new_dict:
                new_dict[singolaparola] = (1, new_dict[singolaparola][1] + 1)
            else:
                new_dict[singolaparola] = (1, 1)

        for campo in new_dict:
            if campo in self.main_dict:
                self.main_dict[campo] = {list(self.main_dict[campo])[0] + new_dict[campo][0],list(self.main_dict[campo])[1] + new_dict[campo][1]}
            else:
                self.main_dict[campo] = {new_dict[campo]}

    def printer(self, filename):
        nome = open(filename, "w")
        for riga in self.main_dict:
            print(riga)
            nome.write(riga)
        nome.close()


def main():
    diz = Contaparole("0001.txt")
    diz.printer("output.txt")


# Esecutore intero progetto
if __name__ == "__main__":
    main()