import re

__author__ = 'Fundor333'


class User:
    lexicon = {}
    document = []

    def __init__(self, documentlist, lexicon):
        for document in documentlist:
            self.document.append(document)
        i = 0
        for word in lexicon:
            self.lexicon[word] = i
            i += 1
        self.userarray(i)

    def userarray(self, maxnum):
        arrayout = [maxnum]
        for element in self.lexicon:
            arrayout.append(0)
        for files in self.document:
            for lines in files:
                for splitted in lines:
                    for word in re.split("[^a-zA-Z]", splitted):
                        if word != '':
                            arrayout[self.lexicon[word]] += 1

        return arrayout

    # TODO sistemare il JSON che ritorna i dati
    def getjson(self):
        stringa = "{testi:["
        i = 0
        for element in self.document:
            if i != 0:
                stringa += ","
            else:
                i += 1
            stringa += '"' + str(element) + '"'
        stringa += "]}"
        return stringa
