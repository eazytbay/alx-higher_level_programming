#!/usr/bin/python3
"""Mylist Module
A class inheriting from list class created
"""


class MyList(list):
    """MyList Class inherits from list"""

    def print_sorted(self):
        """The list printed in ascending order"""

        gen_list = self[:]
        gen_list.sort()
        print("{}".format(gen_list))
