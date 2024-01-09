#!/usr/bin/python3
"""A function that reads from filename and displays its contents to stdout.
    """


def read_file(filename=""):
    """read_file(filename)
    Args:
        filename (str, optional): The filename to be read and printed
        Defaults to "".
    """
    with open(filename, encoding="utf-8") as file:
        info = file.read()
        print(info, end="")
