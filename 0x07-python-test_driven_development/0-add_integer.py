#!/usr/bin/python3
"""one function that calculate addition of two int"""


def add_integer(a, b=98):
    """ function that add two int
        and check if there int or float
        if float cast them to int
        Parameters:
            a: first int or float
            b: second int or float or 98 as default
        Raises:
            TypeError:
                if args not int or float
        Returns:
            result of add
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [float, int]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
