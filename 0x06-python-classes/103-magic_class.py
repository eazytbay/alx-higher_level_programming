#!/usr/bin/python3
"""Magic class utilizing ByteCode."""
import math


class MagicClass:
    """Class representing the MagicClass."""

    def __init__(self, radius=0):
        """Initialize the MagicClass with a given radius."""
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """Calculate and return the circumference of the circle."""
        return 2 * math.pi * self._MagicClass__radius

