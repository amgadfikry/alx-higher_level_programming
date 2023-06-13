#!/usr/bin/python3
""" module convert class to dict"""


def class_to_json(obj):
    """function get dictionary description of class"""

    return vars(obj)
