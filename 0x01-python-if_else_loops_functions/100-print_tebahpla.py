#!/usr/bin/python3
output = ""
for x in range(ord('Z'), ord('A') - 1, -1):
    if x % 2 == 0:
        output += chr(x).lower()
    else:
        output += chr(x).upper()

print("{}".format(output), end='')

