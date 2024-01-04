#!/usr/bin/python3

""" Definition of a rectangle class"""


class Rectangle:
    """ Properties of a rectangle defined"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """gets the property for the width"""
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
        """Gets the property for the height"""
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
                print(self.print_symbol, end='')
            if x is not (self.__height - 1):
                print("")
        return ""

    def __repr__(self):
        """ Displays the rectangle object """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """ Class destructor"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the rectangle with the biggest base on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area() > rect_2.area()):
            return rect_1
        elif (rect_2.area() > rect_1.area()):
            return rect_2
        else:
            return rect_1
