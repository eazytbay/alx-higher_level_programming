#!usr/bin/python3
def replace_in_list(my_list, idx, element):
    # This Checks if idx is negative or out of range
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
    # This replaces the element at the index specified
        my_list[idx] = element
    return my_list
