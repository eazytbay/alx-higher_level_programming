#!/usr/bin/python3
"""Module 0-lookup
Locating the available list attributes & methods of an object
"""


def lookup(obj):
    """Returns the available list of attributes and methods
    Args:
        - obj: The particular object to look into
    """

    return dir(obj)
