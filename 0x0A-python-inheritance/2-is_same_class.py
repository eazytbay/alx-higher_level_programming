#!/usr/bin/python3
"""
A module that contains the function is_same_class
"""


def is_same_class(obj, a_class):
    """return true provided that obj is exactly class a_class,
    otherwise return false"""
    return (type(obj) == a_class)
