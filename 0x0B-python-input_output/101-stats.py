#!/usr/bin/python3
""" python script that read from stdin
    then each line search for status code
    then every 10 line print code, number, size
"""
import sys

size = 0
dic = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
}
row = []
i = 0
try:
    for line in sys.stdin:
        li = line.split(" ")
        try:
            size += int(li[-1])
        except (IndexError, ValueError):
            pass
        try:
            if li[-2] in dic:
                dic[li[-2]] += 1
                if li[-2] not in row:
                    row.append(li[-2])
        except IndexError:
            pass
        i += 1
        if i == 10:
            print(f"File size: {size}")
            for x in sorted(row):
                print(f"{x}: {dic[x]}")
            i = 0
except KeyboardInterrupt:
    print(f"File size: {size}")
    for x in sorted(row):
        print(f"{x}: {dic[x]}")
    raise
