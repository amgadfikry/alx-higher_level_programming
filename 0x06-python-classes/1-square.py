#!/usr/bin/python3
class Square:
    """ class of init attribute only"""
    def __init__(self, size):
        """init method that assign size private
            Args:
                size: size which assign to private size attr
        """
        self.__size = size
