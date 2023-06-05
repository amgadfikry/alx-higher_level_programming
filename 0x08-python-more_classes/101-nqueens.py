#!/usr/bin/python3
import sys
"""module of nqueen that solve puzzle"""

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

if type(int(sys.argv[1])) is not int:
    print("N must be a number")
    sys.exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    sys.exit(1)
