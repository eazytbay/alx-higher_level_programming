#!/usr/bin/python3
output = ""
for x in range(97, 123):
    if chr(x) not in ['q', 'e']:
        output += "{}".format(chr(x))

print(output, end="")
