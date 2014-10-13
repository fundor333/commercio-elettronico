__author__ = 'Fundor333'

class Contaparole:
    nome =""
    fileinput = None
    main_dict = dict()

    def __init__(self,nome):
        self.nome = nome
        self.fileinput = open(nome , 'r')
        for line in self.fileinput:
            self.appoggiodict(line)

    def appoggiodict(self,rigadelfile):
        new_dict = dict()
        rigadelfile.split("")
        for singolaparola in rigadelfile:
            if new_dict.get(singolaparola):
                #TODO add something
        return None


def main():
    Contaparole("../repository/0001.txt")


# Esecutore intero progetto
if __name__ == "__main__":
    main()