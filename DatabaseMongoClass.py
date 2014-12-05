from bson import Code

__author__ = 'Fundor333'

from pymongo import MongoClient


class database():
    db = None

    def __init__(self, name, host, port):
        client = MongoClient(host, port)
        self.db = client[name]

    def getcollection(self, nameofcollection):
        return self.db[nameofcollection]

    def getnamecollection(self):
        return self.db.collection_names()

    def insert(self, nameofcollection, element):
        return self.db[nameofcollection].insert(element)

    def getindex(self, nameofcollection, indexjeson):
        return self.db[nameofcollection].ensure_index(indexjeson)

    def mapreducer(self, mapper, reducer, nomerisultati, collectionname):
        return self.db[collectionname].map_reduce(mapper, reducer, nomerisultati)
