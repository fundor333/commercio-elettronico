__author__ = 'Fundor333'

import logging

import numpy
from scipy.spatial.distance import cosine
from numpy.linalg import svd

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

LEXICONNAME = "./out/out.txt"
USERARRAYNAME = "userarrayname"


def arrayrandom(number):
    return numpy.random.rand(number)


def matrixrandom(xsize, ysize):
    return numpy.random.rand(xsize, ysize)


def multiplayer(array1, array2):
    return numpy.dot(array1, array2)


def distancecof(array1, array2):
    return cosine(array1, array2)


def mysvd(matrix):
    return svd(matrix)


# Esecutore intero progetto
if __name__ == "__main__":
    numberofline = 0
    appoggio = []
    lexicon = (0, {})
    try:
        lexiconnum, lexicondict, numberofline = readlexicon()
        lexicon = (lexiconnum, lexicondict)
    except:
        numberofline = getfromgoogle(NUMERORISULTATI)
        for i in range(0, numberofline):
            inputfile = "./out/" + str(i) + ".txt"
            lexicon = addtolexicon(lexicon, inputfile)
            appoggio.append(inputfile)
    printlexicon(lexicon)