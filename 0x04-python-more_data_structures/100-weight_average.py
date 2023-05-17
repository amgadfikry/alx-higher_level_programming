#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    numbers = sum([x[0] * x[1] for x in my_list])
    weight = sum([x[1] for x in my_list])
    return numbers / weight
