#!/usr/bin/python3
""" Python module student-2 """


class Student(object):
    """Definition Class student"""

    def __init__(self, first_name, last_name, age):
        """__init__ constructor initialized """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionary represt retrieved """
        if attrs is None:
            return self.__dict__
        dictionary = {}
        for access, value in self.__dict__.items():
            if access in attrs:
                dictionary[access] = value
        return dictionary
