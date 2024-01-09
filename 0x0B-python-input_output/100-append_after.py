#!/usr/bin/python3
"""
A function "append after" function
"""


def append_after(filename="", search_string="", new_string=""):
    """This function appends "new_string" after a line containing
    "search_string" in "filename" """
    with open(filename, 'r', encoding='utf-8') as custom_file:
        custom_line_list = []
        while True:
            custom_line = custom_file.readline()
            if custom_line == "":
                break
            custom_line_list.append(custom_line)
            if search_string in custom_line:
                custom_line_list.append(new_string)
    with open(filename, 'w', encoding='utf-8') as custom_file:
        custom_file.writelines(custom_line_list)
