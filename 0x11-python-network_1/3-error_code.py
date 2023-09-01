#!/usr/bin/python3
""" send request to url and mange error http """
from urllib.request import urlopen
from sys import argv
from urllib.error import HTTPError


def main():
    """ function make file not excute if it is not imported """
    try:
        res = urlopen(argv[1])
        print(res.read().decode("utf-8"))
    except HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    main()
