#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    highest = 0
    for key, value in a_dictionary.items():
        if value > highest:
            highest = value
    for key, value in a_dictionary.items():
        if value == highest:
            return key
