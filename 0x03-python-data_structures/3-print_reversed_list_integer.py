#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    new = my_list.reverse()
    for num in new:
        print("{:d}".format(num))
