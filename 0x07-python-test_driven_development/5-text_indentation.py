#!/usr/bin/python3
"""
A python function that prints 2 new lines after the ".?:" characters
"""


def text_indentation(text):
    """ A Function that prints 2 new lines immediately after ".?:" characters
    Args:
        text: string inputed
    Returns:
        Absolutely Nothing
    Raises:
        TypeError: If text is not a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    x = text[:]

    for y in ".?:":
        list_text = x.split(y)
        x = ""
        for a in list_text:
            a = a.strip(" ")
            x = a + y if x is "" else x + "\n\n" + a + y

    print(x[:-3], end="")
