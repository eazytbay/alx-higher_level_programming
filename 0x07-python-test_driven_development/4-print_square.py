#!/usr/bin/python3
"""
A function that uses the"4-print_square" to print a square.

This is a 4-print_square  module that supplies a singlefunction,
print_square(size).
"""

def print_square(size):
    """A square with "#"'s is printed that has a length of size """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
