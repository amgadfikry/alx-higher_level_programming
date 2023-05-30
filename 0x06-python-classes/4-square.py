#!/usr/bin/python3

"""python script to training on classes and oop"""


class Square:
    """square class without any public attributes"""
    def __init__(self, size=0):
        """init methode that start instance with attribute
            size for everyone
            Args:
                size: is size of square may be any data type
        """
        self.__size = size

    @property
    def size(self):
        """getter methode to get size"""
        return self.__size

    @size.setter
    def size(self, num):
        """ setter for size of square and check if digit or not
            and less of 0 or not
            Args:
                num: number to add to size
            """
        if not isinstance(num, int):
            raise TypeError("size must be an intger")
        elif num < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = num

    def area(self):
        """ function that calculate area of square
            Returns: square of size
        """
        return (self.__size * self.__size)
