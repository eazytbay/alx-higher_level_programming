#!/usr/bin/python3
"""locates a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """locates a peak in list_of_integers"""

    if list_of_integers is None or list_of_integers == []:
        return None
    y = 0
    xi = len(list_of_integers)
    mid = ((xi - y) // 2) + y
    mid = int(mid)
    if xi == 1:
        return list_of_integers[0]
    if xi == 2:
        return max(list_of_integers)
    if list_of_integers[mid] >= list_of_integers[mid - 1] and\
            list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
