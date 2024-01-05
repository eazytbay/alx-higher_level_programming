#!/usr/bin/python3
"""
LockedClass
"""

class LockedClass:
    __slots__ = ("first_name",)
     """ No class or object attributes, can't set
        Except for first_name
    """
    def __setattr__(self, name, value):
        if name == "first_name":
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"Cannot set attribute '{name}'")

