#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    li = my_list[:]
    if (idx < 0 or idx > len(my_list)):
        return li
    li[idx] = element
    return li
