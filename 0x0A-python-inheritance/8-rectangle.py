#!/usr/bin/python3
"""
A function that Contains the class Base Geometry and subclass Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represens a rectangle"""
    def __init__(self, width, height):
        """Rectangle instantiation"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
