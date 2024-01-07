#!/usr/bin/python3
"""
A function that divides the numbers or elements of a matrix
"""


def matrix_divided(matrix, div):
    """ This Function that divides the integer/float numbers of a matrix
    Args:
        matrix: list of a lists of integers/floats
        div: number which divides the matrix
    Returns:
        A fresh matrix with the result of the division
    Raises:
        TypeError: If the elements of the matrix are not lists
                   If the elemetns of the lists are neither integers nor floats
                   If div is neither an integer nor float number
                   If the lists of the matrix does not contain the same size
        ZeroDivisionError: If div is zero
    """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    display_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(display_msg)

    size_e = 0
    display_msg_size = "Each row of the matrix must have the same size"

    for items in matrix:
        if not items or not isinstance(items, list):
            raise TypeError(display_msg)

        if size_e != 0 and len(items) != size_e:
            raise TypeError(display_msg_size)

        for dig in items:
            if not type(dig) in (int, float):
                raise TypeError(display_msg)

        size_e = len(items)

    a = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (a)
