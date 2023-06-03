#!/usr/bin/python3
""" function that print all name"""


def say_my_name(first_name, last_name=""):
    """ function that print full name and
        check all if args are strings or not
        Parameters:
            first_name: first name string
            last_name: last name string
        Raises:
            TypeError: if it is not string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
