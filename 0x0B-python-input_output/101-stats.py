#!/usr/bin/python3
import sys
""" module read from input """


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
for line in sys.stdin:

    li = line.split(" ")
    size += int(li[-1])
    if li[-2] in dic:
        dic[li[-2]] += 1
        if li[-2] not in row:
            row.append(li[-2])
    i += 1
    if i == 10:
        print(f"File size: {size}")
        for x in sorted(row):
            print(f"{x}: {dic[x]}")
            i = 0
