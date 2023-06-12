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

    def integer_validator(self, name, value):
        """public instance method that validate value is int
            Parameters:
                name: name of value and it is string
                value: value of name and must be int greater than 0
            Raises:
                ValueError: if value less than or equal to 0
                TypeError: value not int
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value < 1:
            raise ValueError(f"{name} must be greater than 0")
