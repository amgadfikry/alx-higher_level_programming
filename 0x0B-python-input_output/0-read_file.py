#!/usr/bin/python3
""" module that read file"""


def read_file(filename=""):
    """ function read file and print all it's contents"""
    with open(filename, "r", encoding="utf-8") as fi:
        print(fi.read(), end="")
