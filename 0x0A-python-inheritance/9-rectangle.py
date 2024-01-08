#!/usr/bin/python3
"""A Module called 9-rectangle that
Creates a Rectangle class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle Representation
    Private instances attributes:
        - width
        - height
    Public method area()
    Inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """Instances Initialization
        Args:
            - width: rectangle width
            - height: rectangle height
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns a string that has been formatted"""

        return str("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """Evaluates the area of the rectangle instance
        Overwrites the area() method from BaseGeometry
        """

        return self.__width * self.__height
