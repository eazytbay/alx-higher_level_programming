#!/usr/bin/python3
"""Base_Geometry Module
Creates a BaseGeometry class
"""


class BaseGeometry:
    """A Class with public instance methods"""

    def area(self):
        """An Exception is raised with the message
        'area() is not implemented'
        """

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Value is Validated"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
