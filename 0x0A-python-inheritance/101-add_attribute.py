#!/usr/bin/python3
"""
The inclusion of an object
"""


def add_attribute(obj, name, value):
    """
        inclusion of new attribute to object
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
