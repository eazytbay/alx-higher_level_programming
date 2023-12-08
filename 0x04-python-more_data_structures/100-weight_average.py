#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        overall = 0
        weight = 0
        for tots in my_list:
            overall += tots[0] * tots[1]
            weight += tots[1]
        return overall/weight
    return 0
