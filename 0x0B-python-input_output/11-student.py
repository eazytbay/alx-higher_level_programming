#!/usr/bin/python3
"""A student class
    """


class Student:
    """A class defining a student
    """

    def __init__(self, first_name, last_name, age):
        """Initialize the student instance
        Args:
            first_name (string): Student first name
            last_name (string): Student last name
            age (int): Student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary format of the student instance
        Args:
            - attrs: list of attributes
        """

        custom_dict = dict()
        if type(attrs) is list and all(type(item) is str for item in attrs):
            for elem in attrs:
                if elemm in self.__dict__:
                    custom_dict.update({elem: self.__dict__[elem]})
            return custom_dict
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """reload_from_json(json)
        Args:
            json: dictionnary of attributes
        """

        for elemm in json:
            self.__dict__.update({elem: json[elem]})
