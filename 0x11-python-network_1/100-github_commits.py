#!/usr/bin/python3
""" script that git last 5 commits"""
from requests import get
from sys import argv


def main():
    """function to prevent run if imported"""
    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"
    data = get(url).json()
    try:
        for i in range(10):
            print(f"{data[i]['sha']}: {data[i]['commit']['author']['name']}")
    except IndexError:
        pass


if __name__ == "__main__":
    main()
