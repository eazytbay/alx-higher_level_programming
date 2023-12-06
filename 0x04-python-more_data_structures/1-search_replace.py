#!/usr/bin/python3
def search_replace(my_list, search, replace):
    extracted_list = [replace if a == search else a for a in my_list]
    return extracted_list
