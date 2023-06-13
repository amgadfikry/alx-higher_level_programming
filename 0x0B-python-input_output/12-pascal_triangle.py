#!/usr/bin/python3
""" module of pascal triangle """


def pascal_triangle(n):
    """ function make pascal triangle
        Parameters:
            n: number of rows
        Return:
            list of list
    """
    li = []
    if n <= 0:
        return li
    for i in range(n):
        x = [1]
        for j in range(1, i):
            x.append(li[i-1][j-1] + li[i-1][j])
        if i != 0:
            x.append(1)
        li.append(x)
    return li
