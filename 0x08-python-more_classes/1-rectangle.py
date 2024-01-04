#!/usr/bin/python3
"""
Definition of a Rectangle class
"""


class Rectangle:
    """The rectangle representation"""
    def __init__(self, width=0, height=0):
        """The rectangle initialization"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets the attribute width for the private instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the attribute width for the private instance"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets the attribute height for the private instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the attribute height for the private instance"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
