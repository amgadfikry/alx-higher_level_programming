#!/usr/bin/python3

"""python script to training on classes and oop"""


class Square:
    """class init attr and check it number or not"""
    def __init__(self, size=0):
        """init methode that initate instance
            Args:
                size: attr to assign to attr and check it
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
