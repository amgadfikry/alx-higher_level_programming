#!/usr/bin/python3
"""module that define rectangle class with full attributes
    with static, class and instance methods
"""


class Rectangle:
    """Rectangle class with it's methods and attributes"""

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """magic method that print rectanglr as #
            Returns:
                string of # that represent the rectangle
        """
        arr = ""
        if self.__width == 0 or self.__height == 0:
            return arr
        for i in range(self.__height):
            for x in range(self.__width):
                arr += str(self.print_symbol)
            if i != self.__height - 1:
                arr += "\n"
        return arr

    def __repr__(self):
        """magic method that return object representation
            Returns:
                object string representation of instance
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """magic method that print message when delete
            the instance or object
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """static method that compare two instance of rectangle
            Parameters:
                rect_1: first instance of rectangle
                rect_2: second instance of reactangle
            Raises:
                TypeError: if args are not instance of rectangle
            Returns:
                bigger instance or rect1 if are equal
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """class method that make new instance with size
            Parameter:
                size: is size of height and width
            Returns:
                new instance with size
        """
        return cls(size, size)
