#!/usr/bin/python3
"""
A function "0-add_integer" that adds two integers.

The 0-add_integer module supplies one function which is add_integer(a, b).
"""


def add_integer(a, b=98):
    """This returns the addition of two numbers provided."""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
