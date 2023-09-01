#!/usr/bin/python3
""" script fetch data using request package """
from requests import get


def main():
    """ function make file not excute if it is not imported """
    res = get("https://alx-intranet.hbtn.io/status")
    print("""Body response:
\t- type: {}
\t- content: {}""".format(type(res.text), res.text))


if __name__ == "__main__":
    main()
