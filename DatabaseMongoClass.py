__author__ = 'Fundor333'

from pymongo import MongoClient
# Shell for start mongo
# mongod --dbpath Development/commercio-elettronico/mongodb

class databasemongo():
    client = None
    posts = client.posts()

    def __init__(self, host, port):
        self.client = MongoClient(host, port)

    def insertdocument(self, document):
        return self.posts.insert(document)

    def getcollectionnames(self):
        return self.client.collection_names()

    def getquery(self, textquery):
        return self.posts.find_one(textquery)