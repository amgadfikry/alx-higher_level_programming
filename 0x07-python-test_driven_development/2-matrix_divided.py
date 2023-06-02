#!/usr/bin/python3
""" function divides all element in matrix"""


def matrix_divided(matrix, div):
    """ function that divide all numbers in matrix by specific number
        with checking all element in matrix are int or float
        and length of each row is same
        and div number not 0 and is int or float
        Parameters:
            matrix: is array of array
            div: number div elements of matrix
        Raises:
            TypeError: if elements of matrix or div not int or float
            TypeError: if each row of matrix has same length
            ZeroDivisionError: if div number is zero
        Returns:
            new matrix with new values
    """
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list:
        raise TypeError(err_msg)

    if len(matrix) == 0:
        raise TypeError(err_msg)

    first = 0
    arr = []

    for i in matrix:
        subarr = []

        if type(i) is not list:
            raise TypeError(err_msg)

        first = len(matrix[0])
        if len(i) != first:
            raise TypeError("Each row of the matrix must have the same size")

        for x in i:
            if type(x) not in [int, float]:
                raise TypeError(err_msg)

            subarr.append(round(x / div, 2))

        arr.append(subarr)

    return arr
