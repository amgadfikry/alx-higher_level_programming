#!/usr/bin/python3
""" magic class that calculate area  and circumference"""


class MagicClass:
    """ class of magic that can make instance from it"""

    def __init__(self, radius):
        """init of class attr
            check if radius is int or float
            Attr:
                radius: private readius number
        """
        self.__radius = 0 
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """ calculate area of instance
            Returns:
                area value
        """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """calculate circumference by radius
            Return:
                value of circumference
        """
        return 2 * math.pi * self.__radius
