#!/usr/bin/python3
"""module that define rectangle class with full attributes
    with static, class and instance methods
"""


class Rectangle:
    """Rectangle class with it's methods and attributes"""

    def __init__(self, width=0, height=0):
        """init instance method that start at instance
            Parameters:
                width: width of rectangle
                height: height of rectangle
            Attr:
                width: save width paramter in it
                height: save height parameter in it
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width instance getter method
            Returns:
                private attr width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ width instance method setter attribute check
            if integer or less than zero
            Parameters:
                value: value of width
            Raises:
                TypeError: if is not integer
                ValueError: if the value less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height instance getter method
            Returns:
                private attr height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ height instance method setter attribute check
            if integer or less than zero
            Parameters:
                value: value of height
            Raises:
                TypeError: if is not integer
                ValueError: if the value less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """instance method that calculate area of rectangle
            Returns:
                area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """calculate perimeter of rectangle instance method
            Returns:
                perimeter of 0 if width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
