#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for num in matrix:
        for n in range(len(num):
            if (n == len(num) - 1):
                print("{:d}".format(num[n]))
            else:
                print("{:d}".format(num[n]), end=" ")
