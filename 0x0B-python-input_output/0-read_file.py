#!/usr/bin/python3

"""Contains and Reads utf-8 files function and prints it to the stdout"""


def read_file(filename=""):
    """Reads utf-8 files"""

    with open(filename, encoding="utf-8") as f:
        data = f.read()
        print(data, end="")
