#!/usr/bin/python3

"""Appending a string at the end of a text file"""


def append_write(filename="", text=""):
    """A function that appends a string at the end of a text file
    and returns the number of characters added"""

    with open(filename, "+a", encoding="utf-8") as file:
        file_buff = file.write(text)
    return file_buff
