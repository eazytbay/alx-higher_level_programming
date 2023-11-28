#!/usr/bin/python3
for x in range(99):
    print("{} = 0x{:x}".format(x, x), end="\n" if x != 98 else "")
