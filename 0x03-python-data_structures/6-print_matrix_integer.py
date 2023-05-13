#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for num in matrix:
        if type(num) is list:
            for n in num:
                if (n == num[len(num) - 1]):
                    print("{:d}".format(n))
                else:
                    print("{:d}".format(n), end=" ")
        else:
            if (num == matrix[len(matrix) - 1]):
                print("{:d}".format(nun))
            else:
                print("{:d}".format(num), end=" ")
