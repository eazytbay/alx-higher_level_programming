#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary.keys()):
        num = a_dictionary[key]
        print("{}: {}".format(key, num))
