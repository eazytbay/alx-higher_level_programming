#!/usr/bin/python3
"""Module inherits_from
Checks if the object is an instance of a class that inherited
(whether inherited directly/indirectly) from the specified class"""


def inherits_from(obj, a_class):
    """Confirms if obj is an instance of a class that
    inherited from a_class
    Args:
        - obj: The particular object to look at
        - a_class: The class to compute
    Returns: Trueif the obj is a subclass of a_class else reutrn False
    """

    return isinstance(obj, a_class) and type(obj) != a_class
