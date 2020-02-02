#!/usr/bin/env python

"""
Assignment 1 part 1, create and time serial algorithm to multiply matrices

@author Briana Cervantes
"""


import random
from timeit import default_timer as timer

def main():
    """
    Makes function calls to matrix operations and times performance
    """

    a = genMatrix()
    b = genMatrix()

    start = timer()
    c     = multiplyMatrix(a,b)
    end   = timer()
    total = end - start

    printSubMatrix(a)
    printSubMatrix(b)
    printSubMatrix(c)

    print("Time (seconds): %.4f" %total)
    return


def multiplyMatrix(a, b):
    """
    Multiple two square matrices/2d array a and b.

    :param list a: 2d array or matrix
    :param list b: 2d array or matrix
    :return: The result stored in 2d array
    """

    c = [[0 for col in range(len(b[0]))] for row in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                c[i][j] += a[i][k] * b[k][j]
    return c


def printSubMatrix(matrix, n=10):
    """Prints a small portion of the given matrix nth rows and cols"""

    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end = " ")
        print()
    print()


def genMatrix(size=1024, value=1):
    """
    Generates a 2d square matrix of the specified size with the specified values

    Taken from matrixUtils.py
    """

    matrix = [[value for col in range(0,size)] for row in range(0,size)]

    return matrix

main()
