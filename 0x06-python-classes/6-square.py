#!/usr/bin/python3

"""python script to training on classes and oop"""


class Square:
    """Class Square that has attributes. Instantiation with size"""
    def __init__(self, size=0, position=(0, 0)):
        """The __init__ method for Square class
        Args:
             A private instance size
             A private intance position
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """getter function to get size
        Returns:
            The size of the square
        """
        return self.__size

    @property
    def position(self):
        """ getter of position attribute
            Returns:
                value of position
        """
        return self.__position

    @size.setter
    def size(self, value):
        """check errors and setter for size attribute
        Args:
            value: Value to checking errors
        Raises:
            TypeError: Exception if size is not an integer
            ValueError: Exception if size is less than 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """setter of position attribute
            Args:
                value: value of position
            Raises:
                TypeError:if type is no tuple or values is positive
        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of the square
        Returns:
            The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """function that print # accord to square area"""
        if self.__size == 0:
            print("")
        else:
            for z in range(self.position[1]):
                print("")
            for i in range(self.size):
                for x in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print("")
