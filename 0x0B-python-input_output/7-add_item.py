#!/usr/bin/python3
"""A function that saves strings directly from the command line arguments
to file called `add_item.json`. File contains a json serialized list of all strings
entered as arguments to the program.
"""

if __name__ == "__main__":
    import sys
    import json
    save_to_json_file = \
        __import__('7-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('8-load_from_json_file').load_from_json_file

    my_file = "add_item.json"
    with open(my_file, 'a+') as f:  # A add_item.json is created, if necessary
        if f.tell() == 0:
            json.dump([], f)
    data_file = load_from_json_file("add_item.json")
    if len(sys.argv) > 1:
        data_file.extend(sys.argv[1:])
    save_to_json_file(data_file, my_file)
