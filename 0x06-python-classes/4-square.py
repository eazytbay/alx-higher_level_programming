#!/usr/bin/python3
"""Generates a square class for Python
"""


class Square:

    """
    A python class that represents a square.
    """

    def __init__(self, size=0):
        """
        size data initialized.
        """
        self.__size = size

    @property
    def size(self):
        """
        Fetching the size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Initializing both value and type to size. Otherwise raise exceptions.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Evaluates and return the current square area based on given size.
        """
        square_area = self.__size ** 2

        return square_area
