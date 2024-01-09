#!/usr/bin/python3
"""
Reads the "class_to_json" function
"""


def class_to_json(obj):
    """The function returns dictionary described with a simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object"""
    return obj.__dict__
