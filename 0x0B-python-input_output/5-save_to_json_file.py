#!/usr/bin/python3
"""
Reads the "save_to_json_file" function
"""

import json


def save_to_json_file(my_obj, filename):
    """saves an Object to a text file, using a JSON representation"""
    with open(filename, 'w', encoding='utf-8') as x:
        json.dump(my_obj, x)
