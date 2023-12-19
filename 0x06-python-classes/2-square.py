#!/usr/bin/python3
"""Defined square class for Python
"""


class Square:

    """
    Represents a python class with an empty square.
    Initiated with Instantiation with size (no type/value verification).
    """

    def __init__(self, size=0):
        """
        Size data initialized.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
