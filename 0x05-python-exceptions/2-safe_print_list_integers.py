#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    digit = 0
    try:
        for a in range(x):
            if type(my_list[a]) is int:
                print("{:d}".format(my_list[a]), end="")
                digit += 1
    except ValueError and TypeError:
        return
    else:
        print()
        return digit
