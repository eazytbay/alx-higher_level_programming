#!/usr/bin/python3
def safe_function(fct, *args):
    import sys

    try:
        rslt = fct(*args)
    except Exception as incorrect:
        print("Exception: {}".format(incorrect), file=sys.stderr)
        return None
    else:
        return rslt
