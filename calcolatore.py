__author__ = 'Fundor333'


class Contaparole:
    nome = ""
    fileinput = None
    main_dict = None

    def __init__(self, nome, dizionario):
        self.nome = nome
        self.main_dict = dizionario
        self.fileinput = open(nome, 'r')
        dictionary = {}
        for line in self.fileinput:
            self.appoggiodict(line, dictionary)
        self.addDizionario(dictionary)


    def appoggiodict(self, rigadelfile, dictionary):
        for singolaparola in rigadelfile.split():
            if singolaparola in dictionary.keys():
                dictionary[singolaparola] = dictionary[singolaparola] + 1
            else:
                dictionary[singolaparola] = 1


    def addDizionario(self, dizzio):
        for campo in dizzio:
            if campo in self.main_dict.keys():
                self.main_dict[campo] = (
                    self.main_dict[campo][0] + 1, self.main_dict[campo][1] + dizzio[campo])
            else:
                self.main_dict[campo] = (1, dizzio[campo])


    def printer(self, filename):
        nome = open(filename, "w")
        for riga in self.main_dict:
            nome.writelines(riga + str(self.main_dict[riga]) + "\n")
        nome.close()