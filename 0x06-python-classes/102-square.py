#!/usr/bin/python3

"""Google sample style docstrings."""


class Square:
    """Class representing a square."""

    def __init__(self, size=0):
        """Initialize the square with a given size."""
        self.size = size

    def area(self):
        """Calculate and return the area of the square."""
        return (self._size * self._size)

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self._size

    @size.setter
    def size(self, value):
        """Set the size of the square with a given value, raising exceptions if necessary."""
        if type(value) == int:
            if value >= 0:
                self._size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def __eq__(self, other):
        """Check if the area of this square is equal to the area of another square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if the area of this square is not equal to the area of another square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if the area of this square is less than the area of another square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if the area of this square is less than or equal to the area of another square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if the area of this square is greater than the area of another square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if the area of this square is greater than or equal to the area of another square."""
        return self.area() >= other.area()

