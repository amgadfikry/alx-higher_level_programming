#!/usr/bin/python3
""" script send post request with some data """
from requests import post
from sys import argv


def main():
    """ function make file not excute if it is not imported """
    data = {}
    data['email'] = argv[2]
    res = post(argv[1], data=data)
    print(res.text)


if __name__ == "__main__":
    main()
