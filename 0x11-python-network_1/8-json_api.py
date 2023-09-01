#!/usr/bin/python3
""" script fetch json from request """
import requests
from sys import argv


def main():
    """ function make file not excute if it is not imported """
    payload = {"q": ""}
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) > 1:
        payload['q'] = argv[1]
    res = requests.post(url, data=payload)
    try:
        data = res.json()
        if data == {}:
            print("No result")
        else:
            print(f"[{data.get('id')}] {data.get('name')}")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
