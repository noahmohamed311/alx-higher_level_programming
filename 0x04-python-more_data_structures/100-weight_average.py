#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        s = sum([x * y for x, y in my_list])
        average = s / sum([y for x, y in my_list])
        return average
    return 0
