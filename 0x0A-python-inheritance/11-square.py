#!/usr/bin/python3
"""
A function that Contains the class BaseGeometry and subclass Rectangle
"""


class BaseGeometry:
    """A class containing public instance methods area and integer_validator"""
    def area(self):
        """An exception is raised when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """value is validated as an integer that is greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Represents a rectangle"""
    def __init__(self, width, height):
        """Rectangle instantiation"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Represents informal string of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


class Square(Rectangle):
    """Square representation"""
    def __init__(self, size):
        """Square instantiation"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"returns square's area"""
        return self.__size ** 2

    def __str__(self):
        """Represents informal string of the square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
