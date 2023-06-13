#!/usr/bin/python3
""" module append to file"""


def append_write(filename="", text=""):
    """function that append to file"""

    with open(filename, "a", encoding="utf-8") as fi:
        return fi.write(text)
