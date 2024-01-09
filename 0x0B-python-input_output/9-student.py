#!/usr/bin/python3
"""
Read the clas "Student"
"""


class Student:
    """Students Representation"""
    def __init__(self, first_name, last_name, age):
        """Students Initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This returns a dictionary that represents a Student instance"""
        return self.__dict__
