#!/usr/bin/python3

"""Square generating class for Python
"""


class Square:

    """
    A python class representing a square.
    Declared with Private Instance Attribute "size".
    Declared with Private Instance Attribute "position".
    Public instance method "area" returns
    the area of the square based on its size.
    Public instance method "my_print"
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the size and position attributes.
        """
        self.__size = size
        self.__position = position

    def __str__(self):
        """
        String representation method for printing from the main module.
        """
        square_str = ""
        if self.__size == 0:
            return ''
        else:
            square_str += '\n' * self.__position[1]
            for x in range(0, self.__size):
                square_str += ' ' * self.__position[0]
                square_str += '#' * self.__size
                square_str += '\n'
            return square_str[:-1]

    @property
    def size(self):
        """
        Retrieves the size value.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size with a given value and type, raising exceptions if necessary.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the set position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position with a given value, raising exceptions if necessary.
        """

        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")

        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates and returns the current square area based on the given size.
        """
        square_area = self.__size ** 2

        return square_area

    def my_print():
        """
        Prints in stdout the square with the character #
        """
        if self.__size == 0:
            print()
            return

        else:
            for a in range(0, self.__position[1]):
                print()
            for b in range(0, self.__size):
                for c in range(0, self.__position[0]):
                    print(" ", end="")
                for d in range(0, self.__size):
                    print("#", end="")
                print()

