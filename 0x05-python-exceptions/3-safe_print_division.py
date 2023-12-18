#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        Quot = a / b
    except (ZeroDivisionError, FloatingPointError):
        Quot = None
    finally:
        print("Inside result: {}".format(Quot))
    return Quot
