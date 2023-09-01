#!/usr/bin/python3
""" access my github account to git id """
from requests import get
from sys import argv


def main():
    """ function make file not excute if it is not imported """
    url = "https://api.github.com/user"
    res = get(url, auth=(argv[1], argv[2]))
    print(res.json().get('id'))


if __name__ == "__main__":
    main()
