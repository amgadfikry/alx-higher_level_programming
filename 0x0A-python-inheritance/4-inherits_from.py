#!/usr/bin/python3
""" module which check object relations"""


def inherits_from(obj, a_class):
    """ function that check if object is subclass of this class
        directly or indirect
        Parameters:
            obj: object to check
            a_class: parent check is part from it
        Returns:
            true or false
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
