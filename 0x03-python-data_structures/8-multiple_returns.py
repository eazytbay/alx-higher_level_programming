#!/usr/bin/python3
def multiple_returns(sentence):
    length = 0
    first_character = None
    if sentence:
        length = len(sentence)
        first_character = sentence[0]
    return (length, first_character)
