#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if type(my_list) is list:
        li = my_list.copy()
        if (idx < 0 or idx > len(my_list)):
            return li
        li[idx] = element
        return li
    else:
        return None
