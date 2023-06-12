#!/usr/bin/python3
""" module which check object relations"""


def is_kind_of_class(obj, a_class):
    """ function that check if object is instance of specific
        object or class
        Parameters:
            obj: object to check
            a_class: parent check is part from it
        Returns:
            true or false
    """
    return isinstance(obj, a_class)
