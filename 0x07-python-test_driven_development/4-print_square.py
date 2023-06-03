#!/usr/bin/python3
""" function that print square by character of #"""


def print_square(size):
    """function print square by charachter #
        Parameters:
            size: size of square
        Raises:
            TypeError: if size is not int
            ValueError: if size is less than 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print("")

    for i in range(size):
        for x in range(size):
            print("#", end="")
        print("")
