#!/usr/bin/python3
""" script take argv and fetch value in it's header """
from urllib.request import urlopen
from sys import argv


def main():
    """ function make file not excute if it is not imported """
    with urlopen(argv[1]) as res:
        print(res.getheader('X-Request-Id'))


if __name__ == "__main__":
    main()
