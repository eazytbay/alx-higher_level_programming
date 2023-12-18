#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    digit = 0
    try:
        for a in range(0, x):
            print(my_list[a], end="")
            digit += 1
    except (IndexError, TypeError):
        pass
    print()
    return digit
