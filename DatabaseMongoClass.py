__author__ = 'Fundor333'

from pymongo import MongoClient
# Shell for start mongo
# mongod --dbpath Development/commercio-elettronico/mongodb


class database():
    db = None
    posts = None

    def __init__(self, name, host, port):
        client = MongoClient(host, port)
        self.db = client[name]
        self.posts = self.db.posts

    def insertdocument(self, document):
        return self.posts.insert(document)

    def getcollectionnames(self):
        return self.db.collection_names()

    def makequery(self, textquery):
        return self.posts.find_one(textquery)

    def getindex(self, ):
        return self.db.collection.ensureIndex()