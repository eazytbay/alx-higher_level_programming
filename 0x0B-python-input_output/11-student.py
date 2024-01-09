#!/usr/bin/python3
"""
The clasS "Student"
"""


class Student:
    """Definition of class student"""
    def __init__(self, first_name, last_name, age):
        """Student Initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """This returns a dictionary that represents a Student instance
        with the specified attributes"""
        if attrs is None:
            return self.__dict__
        custom_dict = {}
        for x in attrs:
            try:
                custom_dict[x] = self.__dict__[x]
            except:
                pass
        return custom_dict

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for access in json:
            try:
                setattr(self, access, json[access])
            except:
                pass
