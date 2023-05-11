#!/usr/bin/python3
import hidden_4
if (__name__ == "__main__"):
    ls = dir(hidden_4)
    for s in ls:
        if (s[0:2] == "__"):
            continue
        print(f"{s}")
