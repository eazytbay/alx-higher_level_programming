#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copied_list = my_list.copy()
  # Checks the index if it is negative
    if idx < 0:
        return my_list.copy()
  # Checks the index if it is out of range
    if idx > len(my_list) - 1:
        return my_list.copy()
    else:
  # This Replaces the element at the index specified
        copied_list[idx] = element
        return copied_list
