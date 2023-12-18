#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys

    try:
        print("{:d}".format(value))
    except (TypeError, ValueError) as incorrect:
        print("Exception: {}".format(incorrect), file=sys.stderr)
        return False
    else:
        return True
