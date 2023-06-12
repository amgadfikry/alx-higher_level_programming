#!/usr/bin/python3
""" module  of set attribute """


def add_attribute(obj, att, value):
    """ function to set attributes"""

    if type(obj) in [int, str, float, set]:
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, att, value)
