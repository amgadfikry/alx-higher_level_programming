#!/usr/bin/python3
def remove_char_at(str, n):
    st = ""
    for c in range(len(str)):
        if (n == c):
            continue
        st += str[c]
    return st
