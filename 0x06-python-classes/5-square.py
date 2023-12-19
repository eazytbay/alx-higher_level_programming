#!/usr/bin/python3
# 5-square.py

"""Class definition for a Square."""


class Square:
    """Square representation."""

    def __init__(self, __size):
        """square initialization.

        Args:
            __size (int): The __size of the new square.
        """
        self.__size = __size

    @property
    def size(self):
        """Get/set the current __size data of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("__size must be an integer")
        elif value < 0:
            raise ValueError("__size must be >= 0")
        self.__size = value

    def area(self):
        """Return the present area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Displays the square with the # character."""
        for x in range(0, self.__size):
            [print("#", end="") for y in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
