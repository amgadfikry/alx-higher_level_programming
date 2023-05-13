#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)

    def res(ind, len_a, len_b, tub_a, tub_b):
        if len_a >= ind + 1 and len_b >= ind + 1:
            a = tub_a[ind] + tub_b[ind]
        elif len_a >= ind + 1 and len_b <= ind:
            a = tub_a[ind]
        elif len_a <= ind and len_b >= ind + 1:
            a = tub_b[ind]
        else:
            a = 0
        return a
    a = res(0, len_a, len_b, tuple_a, tuple_b)
    b = res(1, len_a, len_b, tuple_a, tuple_b)
    return (a, b)
