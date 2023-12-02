#!usr/bin/python3
def replace_in_list(my_list, idx, element):
    # This checks if idx is a negative value or if it is out of range
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    # This replaces the element at the index specificed
    else:
        my_list[idx] = element
    return my_list
