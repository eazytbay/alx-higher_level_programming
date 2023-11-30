#!/usr/bin/python
def magic_calculation(x, y):
    add, sub = __import__('magic_calculation_102', globals(), locals(), ['add', 'sub']).add, __import__('magic_calculation_102', globals(), locals(), ['add', 'sub']).sub

    if x < y:
        result = add(x, y)
        for i in range(4, 6):
            result = add(result, i)
        return result
    else:
        return sub(x, y)
