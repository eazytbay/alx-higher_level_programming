#!/usr/bin/python3
""" A python module add_item"""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('8-load_from_json_file').load_from_json_file

    try:
        elements = load_from_json_file('add_item.json')
    except FileNotFoundError:
        elements = []
    elements.extend(sys.argv[1:])
    save_to_json_file(elements, 'add_item.json')
