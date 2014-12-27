import re

__author__ = 'Fundor333'


class User:
    lexicon = {}
    document = []
    username = ""

    def __init__(self, documentlist, lexicon, username):
        self.username = username
        for document in documentlist:
            self.document.append(document)
        i = 0
        for word in lexicon:
            self.lexicon[word] = i
            i += 1
        self.userarray(i)

    def userarray(self, maxnum):
        arrayout = [maxnum]
        for _ in self.lexicon:
            arrayout.append(0)
        for files in self.document:
            for lines in files:
                for splitted in lines:
                    for word in re.split("[^a-zA-Z]", splitted):
                        if word != '':
                            arrayout[self.lexicon[word]] += 1

        return arrayout

    def getjson(self):
        # Genera e gestisce un dizionario
        jsondict = {'_id': self.username}
        stringa = []
        for element in self.document:
            stringa.append(element)
        jsondict['text'] = stringa
        return jsondict
