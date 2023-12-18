#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    digit = 0
    try:
        for a in range(x):
            print("{:d}".format(my_list[a]), end="")
            digit = digit + 1
    except:
        print()
        return digit
    else:
        print()
        return digit
