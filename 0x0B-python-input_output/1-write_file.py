#!/usr/bin/python3
""" module write to file """


def write_file(filename="", text=""):
    """ function write to file and create it
        if not exsit
    """

    with open(filename, "w", encoding="utf-8") as fi:
        return fi.write(text)
