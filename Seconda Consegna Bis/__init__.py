from numpy.ma import concatenate, vstack

__author__ = 'Fundor333'

import numpy
from scipy.spatial.distance import pdist

def arrayrandom(number):
    return numpy.random.random(number)


def matrixrandom(xsize, ysize):
    return numpy.random.random(xsize, ysize)


def multiplayer(array1, array2):
    return numpy.dot(array1, array2)

def distancecos(array1, array2):
    z= numpy.vstack([array1,array2])
    return pdist(z,'cosine')


if __name__ == "__main__":
    print(arrayrandom(10))
    print()
    print(distancecos(arrayrandom(10), arrayrandom(10)))