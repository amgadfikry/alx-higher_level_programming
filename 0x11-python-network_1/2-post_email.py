#!/usr/bin/python3
""" send email via post request """
from urllib.request import urlopen
from urllib.parse import urlencode
from sys import argv


def main():
    """ function make file not excute if it is not imported """
    data = {}
    data['email'] = argv[2]
    data_encode = urlencode(data)
    url = f"{argv[1]}?{data_encode}"
    with urlopen(url) as res:
        print(res.read().decode("utf-8"))


if __name__ == "__main__":
    main()
