#!/usr/bin/python3
""" module that represent rectangle class """
from models.base import Base


class Rectangle(Base):
    """ rectangle class that inhereit from base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ init method that initate instance
            Parameters:
                width: width of rectangle
                height: height of rectangle
                x: value of x or 0 if not
                y: value of y or 0 if not
                id: id of class or none if not
            Attr:
                width: private attr of witdth
                height: private attr of height
                x: private attr of x
                y: private attr of y
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getter method for width argument
            Returns:
                private width attr
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter of width argument
            Parameters:
                value: new value of width
            Raises:
                TypeError: if value is not integer
                ValueError: if value less than 1
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 1:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ getter method for height argument
            Returns:
                private height attr
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter of height argument
            Parameters:
                value: new value of height
            Raises:
                TypeError: if value is not integer
                ValueError: if value less than 1
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 1:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ getter method for x argument
            Returns:
                private x attr
        """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter of x argument
            Parameters:
                value: new value of x
            Raises:
                TypeError: if value is not integer
                ValueError: if value less than 0
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ getter method for y argument
            Returns:
                private y attr
        """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter of y argument
            Parameters:
                value: new value of y
            Raises:
                TypeError: if value is not integer
                ValueError: if value less than 0
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ area method that calculate area of rectangle
            Returns:
                area of rectangle
        """
        return (self.width * self.height)

    def display(self):
        """ display method print rectangle instance with
            character '#'
        """
        for y in range(self.y):
            print("")
        for h in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for w in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """ magic method that give string representation of class
            Returns:
                string of class
        """
        text = f"({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
        return "[Rectangle] " + text

    def update(self, *args, **kwargs):
        """ method that update values of arguments of class
            Parameters:
                *args: list of argument
                **kwargs: dictionary of arguemts
        """
        if len(args) > 0:
            for idx, arg in enumerate(args):
                if idx == 0:
                    self.id = arg
                elif idx == 1:
                    self.width = arg
                elif idx == 2:
                    self.height = arg
                elif idx == 3:
                    self.x = arg
                elif idx == 4:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "id":
                    self.id = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ public method that convert class to dictionary
            representation
            Returns:
                dictionary of class
        """
        dic = vars(self)
        dic_t = {key.split("_")[-1]: value for key, value in dic.items()}
        return dic_t
