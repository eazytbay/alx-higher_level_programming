#!/usr/bin/python3
"""A Python Module that writes to a file
    """


def write_file(filename="", text=""):
    """A function write_file(filename, text)
    Args:
        filename (str, optional): The Name of the file, with its extension.
        Defaults to "".
        text (str, optional): String to write to the file. Defaults to "".
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
