#!/usr/bin/python3
""" script get some value from header of request """
from requests import get
from sys import argv


def main():
    """ function make file not excute if it is not imported """
    res = get(argv[1])
    print(res.headers.get("X-Request-Id"))


if __name__ == "__main__":
    main()
