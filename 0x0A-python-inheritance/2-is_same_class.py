#!/usr/bin/python3
""" module which check object relations"""


def is_same_class(obj, a_class):
    """ function that check if object is instance of specific
        object or not
        Parameters:
            obj: object to check
            a_class: parent check is part from it
        Returns:
            true or false
    """
    return type(obj) == a_class
