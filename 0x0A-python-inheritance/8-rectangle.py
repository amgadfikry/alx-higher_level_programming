#!/usr/bin/python3
""" module of of subclass rectangle"""
p_cls = __import__("7-base_geometry").BaseGeometry


class Rectangle(p_cls):
    """ subclass that import class of basegeometry"""

    def __init__(self, width, height):
        """ init method that declare attribute with validation
            Attr:
                width: width of rect
                height: height of rect
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
