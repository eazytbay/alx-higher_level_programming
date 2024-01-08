#!/usr/bin/python3
"""A Module is_kind_of_class
Confirms if the object is an instance of, or if it is an
instance of a class that inherited from, the particular class
"""


def is_kind_of_class(obj, a_class):
    """Confirms if obj is an instance of a_class or a class
    inherited from a_class
    Args:
        - obj: The object to look at or check
        - a_class:  The class to evaluate 
    Returns: True if the obj is an instance of a class else False
    """

    return isinstance(obj, a_class)
