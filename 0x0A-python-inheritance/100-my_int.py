#!/usr/bin/python3
"""A Module 100-my_int that
Creates a class that inherits from int
"""


class MyInt(int):
    """inheriting class from int,
    Characterised by the opposite behaviour of != and ==
    """

    def __eq__(self, other):
        """What was Equal now becomes Unequal"""

        return super().__ne__(other)

    def __ne__(self, other):
        """What was Unequal now becomes Equal """

        return super().__eq__(other)
