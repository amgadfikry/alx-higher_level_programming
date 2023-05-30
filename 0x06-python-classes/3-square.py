#!/usr/bin/python3

"""python script to training on classes and oop"""


class Square:
    """class to identify size and square"""
    def __init__(self, size=0):
        """init method with instance size
            Args:
                size: size of square
        """
        if not isinstance(size, int):
            raise ValueError("size must be an intger")
        elif size < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """area method that calculate area of square
            Returns:
                area of square
        """
        return (self.__size * self.__size)
