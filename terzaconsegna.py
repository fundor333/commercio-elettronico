__author__ = 'Fundor333'

import linecache

from DatabaseMongoClass import database
from primaconsegna import getfromgoogle, NUMERORISULTATI, OUTPITFILENAME

INSERITO = 1
NAMEDB = "Silvestri"
DBM = database(NAMEDB, 'localhost', 27017)


def elaboratejson(texts, namefile):
    return {"_id": namefile, "body": texts}


def main():
    if INSERITO == 0:
        try:
            fistline = linecache.getline("./out/" + OUTPITFILENAME + ".txt", 1)
            print("Ho recuperato i documenti")
        except IOError:
            fistline = getfromgoogle(NUMERORISULTATI)
            print("Ho recuperato i documenti")

        print("Ecco gli ID dei documenti")
        print("##############")

        for i in range(0, int(fistline)):
            textappend = ""
            fileinname = "./out/" + str(i) + ".txt"
            filein = open(fileinname)
            for line in filein:
                textappend += line
            print(DBM.insertdocument(elaboratejson(textappend, fileinname)))

        print("##############")
        print("Fine degli ID nei documenti")

    print("Elaboro i dati")
    indexdb = DBM.getindex("{'body': 'text'}")
    print(indexdb)

if __name__ == "__main__":
    main()