#!/usr/bin/python3
""" module for square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class inherit all from rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ init new class with same as rectangle class
            Parameters:
                size: is represent width and height of square
                x: x axis of square
                y: y axis of square
                id: id of new instance
            Attr:
                width: width of square which is size
                height: height of quare which is size
                x: x axis of square
                y: y axix of square
                id: id of new class instance
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ getter of size attribute value """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter for new value of size attribute
            Parameters:
                value: new value of size
        """
        self.width = value
        self.height = value
        self.__size = value

    def __str__(self):
        """ magic method that repesent class in string
            Returns:
                string representation of class
        """
        text = f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
        return text

    def update(self, *args, **kwargs):
        """ public method that update attributes of class instance
            Parameters:
                args: list of new values
                kwargd: dictionary of new values
        """
        if len(args) > 0:
            for idx, arg in enumerate(args):
                if idx == 0:
                    self.id = arg
                if idx == 1:
                    self.size = arg
                    self.width = arg
                    self.height = arg
                if idx == 2:
                    self.x = arg
                if idx == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                    self.width = value
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """ public method that get dictionary representation of
            instance
            Returns:
                dictionary of class
        """
        dic = vars(self)
        dic_x = {}
        for key, value in dic.items():
            k = key.split("_")[-1]
            if k in ["height", "width"]:
                continue
            dic_x[k] = value
        return dic_x
