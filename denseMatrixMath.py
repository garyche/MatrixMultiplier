#!/bin/pyhton
### BY: GARY CHEUNG AND DEV SETHI

from sparseMatrixMath import createEmptyMatrix
from sparseMatrixDemo import matrixDisplay


#Placeholder matricies to test instead of matricies passed into function
#matrix1= [[1,2,3],[4,5,6]]
#matrix2= [[4,5,6],[7,8,9]]

def addMatricies(matrix1, matrix2):
    """ adds two matricies of equal size together, displays sum and returns sum as list of lists """

    matrixOut = createEmptyMatrix(len(matrix1),len(matrix1[0]))
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            matrixOut[i][j] = matrix1[i][j] + matrix2[i][j]
    return matrixOut
