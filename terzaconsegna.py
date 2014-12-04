__author__ = 'Fundor333'

import linecache

from DatabaseMongoClass import database
from primaconsegna import getfromgoogle, NUMERORISULTATI, OUTPITFILENAME

INSERITO = 0
NAMEDB = "Silvestri"
DBM = database(NAMEDB, 'localhost', 27017)
COLLECTIONNAME = "Documenti"


def elaboratoretesti(texts, namefile):
    return {"_id": namefile, "body": texts}


def main():
    try:
        openfile= open("./out/" + OUTPITFILENAME + ".txt")
        fistline = linecache.getline(openfile, 1)
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
    indexdb = DBM.getindex(COLLECTIONNAME, "{'body': 'text'}")
    print(indexdb)

if __name__ == "__main__":
    main()