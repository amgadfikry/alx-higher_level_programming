#!/usr/bin/python3
""" module of parent class and subclasses """


class BaseGeometry:
    """ basegeometry is parent class"""

    def area(self):
        """ public instance method that raise exception
            Raise:
                area() is not found
        """
        raise Exception("area() is not implemented")
