#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = sorted(a_dictionary.keys())
    for x in keys:
        print(f"{x}: {a_dictionary[x]}")
