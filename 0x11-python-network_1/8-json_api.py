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
    res = requests.post(url, params=payload)
    if res.headers.get("content-type") == "application/json":
        data = res.json()
        if data:
            print(f"[{data.get('id')}] {data.get('name')}")
        else:
            print("No result")
    else:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
