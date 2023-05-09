#!/usr/bin/python3
def uppercase(str):
    st = ""
    for c in str:
        if (ord(c) > 96 and ord(c) < 123):
            st += chr(ord(c) - 32)
        else:
            st += c
    print("{}".format(st))
