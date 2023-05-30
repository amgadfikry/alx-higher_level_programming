#!/usr/bin/python3
class Square:
    """class init attr and check it number or not"""
    def __init__(self, size=0):
        """init methode that initate instance 
            Args:
                size: attr to assign to attr and check it
        """
        if not isinstance(size, int):
            raise ValueError("size must be an intger")
        elif size < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = size
