#!/usr/bin/python3
def new_in_list(my_list, idx, element):
  # Checks the index if it is negative
  if idx < 0:
    return my_list[:]
  # Checks the index if it is out of range
  if idx > len(my_list):
    return my_list[:]
  # This Creates a copy of the original list
  copied_list = my_list[:]
  # This Replaces the element at the index specified
  copied_list[idx] = element
  return copied_list
