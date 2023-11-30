#!/usr/bin/python3
    
if __name__ == "__main__":
    """DIsplay the exact list and number of the arguments"""
    import sys
    n_arg = len(sys.argv) - 1

    if n_arg == 0:
        print("0 arguments.")
    elif n_arg == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(n_arg))

    for i in range(n_arg):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
