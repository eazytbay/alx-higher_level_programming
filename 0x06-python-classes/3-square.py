#!/usr/bin/python3
# 3-square.py

"""class Square defined."""


class Square:
    """Connotes a square."""

    def __init__(self, __size=0):
        """Indicates that a new square has been initialized.

        Args:
            __size (int): The __size data has been initialized.
        """
        if not isinstance(__size, int):
            raise TypeError("__size must be an integer")
        elif __size < 0:
            raise ValueError("__size must be >= 0")
        self.__size = __size

    def area(self):
        """Return the present area of the square."""
        return (self.__size * self.__size)
