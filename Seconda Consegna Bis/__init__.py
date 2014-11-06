__author__ = 'Fundor333'

import numpy
from scipy.spatial.distance import cosine
from numpy.linalg import svd


def arrayrandom(number):
    return numpy.random.rand(number)


def matrixrandom(xsize, ysize):
    return numpy.random.rand(xsize, ysize)


def multiplayer(array1, array2):
    return numpy.dot(array1, array2)

def distancecof(array1, array2):
    return cosine(array1,array2)

def mysvd(matrix):
    return svd(matrix)

if __name__ == "__main__":
    a = matrixrandom(300,300)
    print(mysvd(a))