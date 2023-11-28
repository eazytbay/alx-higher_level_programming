#!/usr/bin/python3
def uppercase(s):
    result = ""  # Initialize an empty string to store the result
    for char in s:
        if 97 <= ord(char) <= 122:
            result += "{}".format(chr(ord(char) - 32))
        else:
            result += "{}".format(char)
    print(result)
