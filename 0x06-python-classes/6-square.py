#!/usr/bin/python3

"""Definition of class for Python
"""


class Square:
    """Connotes a square.
    Private instance attribute: size:
        - property def size(self)
        - sets property for def size(self, value)
    Private instance attribute: position:
        - property def position(self)
        - sets property for def position(self, value)
    Instantiation with the optional size and optional position.
    Public instance method: def area(self).
    Public instance method: def my_print(self).
    """

    def __init__(self, size=0, position=(0, 0)):
        """data initialized."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """size retrieval."""
        return self.__size

    @size.setter
    def size(self, value):
        """Initializes the size to a value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """position retrieval."""
        return self.__position

    @position.setter
    def position(self, value):
        """initializes the position to a value."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the presents square area."""
        return self.__size ** 2

    def my_print(self):
        """Outputs to stdout the square with the character #,
        at the exact position given by the position attribute.
        """
        if self.__size == 0:
            print()
            return
        for x in range(0, self.__position[1]):
            print()
        for a in range(0, self.__size):
            for b in range(0, self.__position[0]):
                print(" ", end="")
            for c in range(0, self.__size):
                print("#", end="")
            print()
