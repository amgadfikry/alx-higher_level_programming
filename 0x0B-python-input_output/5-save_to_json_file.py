#!/usr/bin/python3
""" module to convert to json in file"""
import json


def save_to_json_file(my_obj, filename):
    """function that convert obj to json and add
        it to file
    """
    with open(filename, "w", encoding="utf-8") as fi:
        fi.write(json.dumps(my_obj))
