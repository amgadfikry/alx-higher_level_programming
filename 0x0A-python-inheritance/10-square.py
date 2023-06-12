#!/usr/bin/python3
""" module of subclass of rectangle"""
p_cls = __import__("9-rectangle").Rectangle


class Square(p_cls):
    """class of square inherited from recatangle class
        which inherit from basegeometry
    """

    def __init__(self, size):
        """init method that start attribute
            Attr:
                size: size of square
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
