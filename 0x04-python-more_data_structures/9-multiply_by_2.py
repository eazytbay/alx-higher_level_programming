#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    custom_dict = dict()
    for key in a_dictionary.keys():
        custom_dict[key] = a_dictionary[key] * 2
    return custom_dict
