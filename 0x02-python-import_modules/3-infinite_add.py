#!/usr/bin/python3
import sys
if (__name__ == "__main__"):
    sum = 0
    if (len(sys.argv) == 1):
        print(f"{sum:d}")
    else:
        for arg in sys.argv:
            if (sys.argv.index(arg) == 0):
                continue
            sum += int(arg)
        print(f"{sum:d}")
