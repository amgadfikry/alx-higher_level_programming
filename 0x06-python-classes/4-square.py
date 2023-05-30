#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, num):
        if not isinstance(num, int):
            raise ValueError("size must be an intger")
        elif num < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = num

    def area(self):
        return (self.__size * self.__size)
