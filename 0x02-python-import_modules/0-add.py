#!/usr/bin/python3
def add(a, b):
    return a + b
if __name__ == "__main__":
    a = 1
    b = 2
    from add_0 import add as add_0
    result = add_0(a, b)
    print("{} + {} = {}".format(a, b, result))
