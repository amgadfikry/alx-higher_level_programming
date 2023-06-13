#!/usr/bin/python3
""" module to convert to python obj in file"""
import json


def load_from_json_file(filename):
    """function that convert strin file to
        json
    """
    with open(filename, "r", encoding="utf-8") as fi:
        return json.loads(fi.read())
