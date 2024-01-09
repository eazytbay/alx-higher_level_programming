#!/usr/bin/python3
"""
Reads the function "write_file"
"""


def write_file(filename="", text=""):
    """This function returns the exact number of charas written to "filename" from "text" """
    with open(filename, 'w', encoding='utf=8') as x:
        return x.write(text)
