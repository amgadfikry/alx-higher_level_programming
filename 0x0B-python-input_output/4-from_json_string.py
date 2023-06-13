#!/usr/bin/python3
""" module that convert str to obj"""
import json


def from_json_string(my_str):
    """function that deserialized obj"""

    return json.loads(my_str)
