__author__ = 'Fundor333'

from pymongo import MongoClient


class database():
    db = None

    def __init__(self, name, host, port):
        client = MongoClient(host, port)
        self.db = client[name]

    def getcollection(self, namecollection):
        return self.db[namecollection]

    def insert(self, nameofcollection, element):
        collection = self.getcollection(nameofcollection)
        return collection.insert(element)

    def getcollectionnames(self):
        return self.db.collection_names()