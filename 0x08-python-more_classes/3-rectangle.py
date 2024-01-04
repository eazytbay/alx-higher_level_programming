#!/usr/bin/python3

""" A rectangle class"""


class Rectangle:
    """ Definition the attributes of a rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the property of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the property of the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the property of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the property of the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Evaluates the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Evaluates the perimeter of the rectangle"""
        if self.__width and self.__height:
            return 2*(self.__width + self.__height)
        return 0

    def __str__(self):
        """A display of the rectangle using a pictorial format using #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        for x in range(self.__height):
            for y in range(self.__width):
                print("#", end='')
            if x is not (self.__height - 1):
                print("")
        return ""
