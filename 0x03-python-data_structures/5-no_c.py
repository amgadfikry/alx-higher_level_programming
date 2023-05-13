#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for c in my_string:
        if (c == "c" or c == "C"):
            continue
        new += c
    return new
