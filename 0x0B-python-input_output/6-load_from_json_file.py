#!/usr/bin/python3
"""
Reads the "load_from_json_file" function
"""

import json


def load_from_json_file(filename):
    """Writes and creates an Object from a "JSON file" """
    with open(filename, 'r', encoding='utf-8') as x:
        return json.load(x)
