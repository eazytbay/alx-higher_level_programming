#!/usr/bin/python3
"""
A module that Contains the class Base Geometry
"""


class BaseGeometry:
    """Definition of a  class with public attribute area"""
    def area(self):
        """An exception is raised when called"""
        raise Exception("area() is not implemented")
