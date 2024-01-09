#!/usr/bin/python3
"""
Pasacal triangle that creates list of lists is defined
"""


def pascal_triangle(n):
    """
    triangle module defined
    """
    if n <= 0:
        return []
    ephem = []
    custom_list = []
    for x in range(n):
        row = []
        for y in range(x + 1):
            if x == 0 or y == 0 or x == y:
                row.append(1)
            else:
                row.append(custom_list[y] + custom_list[y - 1])
        custom_list = row
        ephem.append(row)
    return ephem
