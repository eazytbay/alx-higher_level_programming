#!/usr/bin/python3

""" A rectangle class"""


class Rectangle:
    """ Definition the properties of a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Sets the property of the wdith"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the property of the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets the property of the height"""
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
        """Displays the rectangle in pictorial format using #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        for x in range(self.__height):
            for y in range(self.__width):
                print("#", end='')
            if x is not (self.__height - 1):
                print("")
        return ""

    def __repr__(self):
        """Displays the rectangle object """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Class  destructor"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
