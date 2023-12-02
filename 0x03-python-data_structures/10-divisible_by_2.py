#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    filtered_list = []
    for x in range(len(my_list)):
        if my_list[x] % 2 == 0:
            filtered_list.append(True)
        else:
            filtered_list.append(False)
    return filtered_list
