#!/usr/bin/python3

"""python script to training on classes and oop"""


class Square:
    """Class Square that has attributes. Instantiation with size"""
    def __init__(self, size=0):
        """The __init__ method for Square class
        Args:
             A private instance size
        """
        self.__size = size

    @property
    def size(self):
        """getter function to get size
        Returns:
            The size of the square
        """
        return self.__size

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
            for i in range(self.__size):
                for i in range(self.__size):
                    print("#", end="")
                print("")

