#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if (__name__ == "__main__"):
    if (len(sys.argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        op = {"+": add, "-": sub, "*": mul, "/": div}
        for o, x in op.items():
            if (sys.argv[2] == o):
                print(f"{a:d} {o} {b:d} = {x(a, b):d}")
                exit(0)
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
