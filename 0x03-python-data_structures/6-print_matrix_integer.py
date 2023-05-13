#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for num in matrix:
        for n in num:
            if (n == num[len(num) - 1]):
                print("{:d}".format(n))
            else:
                print("{:d}".format(n), end=" ")
