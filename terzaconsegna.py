__author__ = 'Fundor333'

import linecache

from DatabaseMongoClass import database
from primaconsegna import getfromgoogle, NUMERORISULTATI, OUTPITFILENAME

INSERITO = 0
NAMEDB = "Silvestri"
DBM = database(NAMEDB, 'localhost', 27017)


def elaboratejson(texts, namefile):
    return {"filename": namefile, "text": texts}


def main():
    try:
        fistline = linecache.getline("./out/" + OUTPITFILENAME + ".txt", 1)
    except IOError:
        fistline = getfromgoogle(NUMERORISULTATI)

    if INSERITO == 0:
        for i in range(0, int(fistline)):
            textappend = ""
            fileinname = "./out/" + str(i) + ".txt"
            filein = open(fileinname)
            for line in filein:
                textappend += line
            print(DBM.insertdocument(elaboratejson(textappend, fileinname)))


if __name__ == "__main__":
    main()