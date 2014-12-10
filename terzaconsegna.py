from bson import Code
import pymongo

from userterzaconsegna import User


__author__ = 'Fundor333'

import linecache

from DatabaseMongoClass import database
from primaconsegna import getfromgoogle, NUMERORISULTATI, OUTPITFILENAME


INSERITO = 1
NAMEDB = "Silvestri"
DBM = database(NAMEDB, 'localhost', 27017)
COLLECTIONNAME = "documenti"
LEXICON = []


def elaboratoretesti(texts, namefile):
    return {"_id": namefile, "body": texts}


def main():
    try:
        open("./out/" + OUTPITFILENAME + ".txt")
        fistline = linecache.getline("./out/" + OUTPITFILENAME + ".txt", 1)
        print("Ho recuperato i documenti")
    except IOError:
        fistline = getfromgoogle(NUMERORISULTATI)
        print("Ho generato i documenti")
    if INSERITO == 0:
        print("Ecco gli ID dei documenti")
        print("##############")

        for i in range(0, int(fistline)):
            textappend = ""
            fileinname = "./out/" + str(i) + ".txt"
            filein = open(fileinname)
            for line in filein:
                textappend += line
            print(DBM.insert(COLLECTIONNAME, elaboratoretesti(textappend, fileinname)))

        print("##############")
        print("Fine degli ID nei documenti")
    print("Elaboro i dati")
    mapper = Code(open('mapper.js', 'r').read())
    reducer = Code(open('reducer.js', 'r').read())
    reduction = DBM.mapreducer(mapper, reducer, "risultati", COLLECTIONNAME)
    print("Frequenza delle parole")
    fileout = open("terzaout.txt", 'w')
    outlexicon = open("lexicon.txt", 'w')
    for element in reduction.find():
        fileout.write(str(element['_id']) + " " + str(element['value']) + '\n')
        LEXICON.append(str(element['_id']))
        outlexicon.write(str(element['_id']) + '\n')
    fileout.close()
    outlexicon.close()
    for line in reduction.find().sort("value", pymongo.DESCENDING).limit(10):
        print line['_id']
    documentlist = {"./out/7.txt", "./out/6.txt", "./out/5.txt", "./out/4.txt", "./out/3.txt", "./out/2.txt",
                    "./out/1.txt", "./out/0.txt"}
    utente = User(documentlist, LEXICON)
    print(utente.getjson())
    # DBM.insert("user", utente.getjson)

if __name__ == "__main__":
    main()