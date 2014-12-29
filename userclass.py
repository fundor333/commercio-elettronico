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

    def getjson(self):
        # Genera e gestisce un dizionario
        jsondict = {'_id': self.username}
        stringa = []
        for element in self.document:
            stringa.append(element)
        jsondict['text'] = stringa
        return jsondict
