#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = ()
    a_padded = tuple_a + (0,) * (2 - len(tuple_a))
    b_padded = tuple_b + (0,) * (2 - len(tuple_b))
    for x in range(2):
        result += (a_padded[x] + b_padded[x],)
    return result
