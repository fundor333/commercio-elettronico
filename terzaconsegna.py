__author__ = 'Fundor333'

from pymongo import MongoClient
# Shell for start mongo
# mongod --dbpath Development/commercio-elettronico/mongodb


class databaseMongo():
    client = MongoClient('localhost', 27017)

    def __init__(self, dbname):
        self.db = self.client[dbname]


def main():
    databaseMongo("provaDB")


if __name__ == "__main__":
    main()