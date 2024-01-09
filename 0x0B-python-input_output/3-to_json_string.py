#!/usr/bin/python3
"""
Reads the "to_json_string" function
"""

import json


def to_json_string(my_obj):
    """This function returns the JSON representation of an object (string)"""
    return json.dumps(my_obj)
