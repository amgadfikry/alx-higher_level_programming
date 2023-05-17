#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mat = []
    for x in matrix:
        mat.append(list(map(lambda y: y * y, x)))
    return mat
