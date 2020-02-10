#!/usr/bin/env python

"""
Assignment 1 part 1 and 2, create and time serial and parallel  algorithm to multiply matrices

@author Briana Cervantes
"""

import numpy as np
import pymp as mp
import argparse
import matrixUtils as mu
from timeit import default_timer as timer


def multiplyMatrix(matrixA, matrixB):
    """
    Multiple two square matrices/2d array a and b, serial algorithm.
    """

    matrixC= [[0 for col in range(len(b[0]))] for row in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                matrixC[i][j] += matrixA[i][k] * matrixB[k][j]
    return c


def parallelMultiply(matrixA, matrixB,num_threads):
    """
    Parallel algrorithm to multiple square matrix a and b.
    """
    
    size = len(matrixA)
    matrixC = mp.shared.array((size, size), dtype=int)
    
    #number of theads to be specified through terminal
    for i in range(0,size):
        with mp.Parallel(num_threads) as p:
            for j in p.range(0,len(matrixB[0])):
                for k in range(0,size):
                    matrixC[i][j] += matrixA[i][k] * matrixB[k][j]    
    return matrixC


def serialTest():
    """
    Tests and times serial algorithm for matrix multiplication. Output sent to serialOut.txt
    """
    
    #accumulator
    total = 0

    #get average time
    for i in range(0,5):
        start   = timer()
        matrixC = MultiplyMatrix(matrixA, matrixB)
        end     = timer()
        total  += end - start
        
    #Prints average performance time
    print('Total time: %.4f' %(total/10))
    return matrixC
    
    
def parallelTest(matrixA, matrixB, num_threads):
    #accumulator
    total = 0

    #get average time
    for i in range(0,5):
        start   = timer()
        matrixC = parallelMultiply(matrixA, matrixB, num_threads)
        end     = timer()
        total  += end - start 
    #Prints average performance time
    print('Total time: %.4f' %(total/5))
    return matrixC


def main():
    """
    Used for running as a script
    """

    parser = argparse.ArgumentParser(description=
        'Generate a 2d matrix and save it to a file.')
    parser.add_argument('-e','--serial', action='store_true',
        help='Tests the serial algorithm')
    parser.add_argument('-p','--parallel', action='store_true',
        help='Tests the parallel algorithm')
    parser.add_argument('-n','--num_of_threads', default=1, type=int,
        help='Number of threads used in the parallel algorithm')
    parser.add_argument('-s', '--size', default=700, type=int,
        help='Size of the 2d matrix to generate')
    parser.add_argument('-v', '--value', default=1, type=int,
        help='The value with which to fill the array with')
    parser.add_argument('-f', '--filename', default='output.txt', type=str,
        help='The name of the file to save the matrix in (optional)')

    args = parser.parse_args()

    matrixA = mu.genMatrix2(args.size, args.value)
    matrixB = mu.genMatrix2(args.size, args.value)

    if args.parallel is not None:
        matrixC = parallelTest(matrixA, matrixB, args.num_of_threads)
    else:
        matrixC = serialTest(matrixA, matrixB)
    
    if args.filename is not None:
        print(f'Writing matrix to {args.filename}')
        mu.writeToFile(matrixC, args.filename)

        print(f'Testing file')
        mu.printSubarray(mu.readFromFile(args.filename))
    else:
        mu.printSubarray(matrixC)
    return

        
if __name__ == '__main__':
    # execute only if run as a script
    main()
