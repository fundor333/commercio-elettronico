__author__ = 'Fundor333'

import linecache

from DatabaseMongoClass import database
from primaconsegna import getfromgoogle, NUMERORISULTATI, OUTPITFILENAME

DBM = database('localhost', 27017)


def elaboratejson(texts, namefile):
    return {"filename": namefile, "text": texts}


def main():
    try:
        fistline = linecache.getline(OUTPITFILENAME + ".txt", 1)
    except IOError:
        fistline = getfromgoogle(NUMERORISULTATI)

    for i in range(0, int(fistline)):
        textappend = ""
        fileinname = "./out/" + str(i) + ".txt"
        filein = open(fileinname)
        # todo Generazione dei testi in JSON
        for line in filein:
            textappend += line
        print(DBM.insertdocument(elaboratejson(textappend, fileinname)))


if __name__ == "__main__":
    main()