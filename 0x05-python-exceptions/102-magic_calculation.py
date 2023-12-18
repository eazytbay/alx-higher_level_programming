#!/usr/bin/python3
import sys


def magic_calculation(a, b):
    computed_output = 0
    for x in range(1, 3):
        try:
            if x > a:
                raise Exception('Too far')
            else:
                computed_output += (a ** b) / x
        except Exception as error:
            computed_output = b + a
            break
    return computed_output
