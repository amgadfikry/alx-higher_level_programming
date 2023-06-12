#!/usr/bin/python3
""" module that get list of object content """


def lookup(obj):
    """ function that get list of object attributes
        and method
        Parameters:
            obj: object
        Returns:
            list of attribures and methods
    """
    return dir(obj)
