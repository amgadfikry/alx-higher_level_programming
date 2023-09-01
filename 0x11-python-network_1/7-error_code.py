#!/usr/bin/python3
""" script check if there error in status code """
from requests import get
from sys import argv


def main():
    """ function make file not excute if it is not imported """
    res = get(argv[1])
    if res.status_code > 399:
        print(f"Error code: {res.status_code}")
    else:
        print(res.text)


if __name__ == "__main__":
    main()
