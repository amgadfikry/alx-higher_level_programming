#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []
    for x, y in enumerate(my_list):
        if y == search:
            new.append(replace)
            continue
        new.append(y)
    return new
