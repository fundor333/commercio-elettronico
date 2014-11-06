from numpy.ma import concatenate, vstack

__author__ = 'Fundor333'

import numpy
from scipy.spatial.distance import cosine

def arrayrandom(number):
    return numpy.random.random(number)


def matrixrandom(xsize, ysize):
    return numpy.random.random(xsize, ysize)


def multiplayer(array1, array2):
    return numpy.dot(array1, array2)

def distancecof(array1, array2):
    return cosine(array1,array2)


if __name__ == "__main__":
    print(arrayrandom(10))
    print()
    print(distancecof(arrayrandom(10), arrayrandom(10)))