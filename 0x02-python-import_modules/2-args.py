#!/usr/bin/python3
import sys
if (__name__ == "__main__"):
    if (len(sys.argv) ==  1):
        print("0 arguments.")
    else:
        print(f"{len(sys.argv) - 1} arguments:")
        i = 0
        for arg in sys.argv:
            if (i == 0):
                i += 1
                continue
            print(f"{i}: {arg}")
            i += 1

