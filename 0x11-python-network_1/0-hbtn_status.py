#!/usr/bin/python3
""" script that fetch data using urllib """
import urllib.request


def main():
    """ function make file not excute if it is not imported """
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as res:
        body = res.read()
        print("""Body response:
    - type: {}
    - content: {}
    - utf8 content: {}""".format(
                type(body),
                body,
                body.decode("utf-8")))


if __name__ == "__main__":
    main()
