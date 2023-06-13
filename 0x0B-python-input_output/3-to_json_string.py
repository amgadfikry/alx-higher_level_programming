#!/usr/bin/python3
""" module that convert obj to str"""
import json


def to_json_string(my_obj):
    """function that serialized obj"""

    return json.dumps(my_obj)
