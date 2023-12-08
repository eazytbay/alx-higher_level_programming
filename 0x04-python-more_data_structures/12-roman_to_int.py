#!/usr/bin/python3
def roman_to_int(roman_string):
    outcome = 0
    end = 0
    digit = (('I', 1), ('V', 5), ('X', 10),
                ('L', 50), ('C', 100), ('D', 500),
                ('M', 1000))
    if type(roman_string) is not str:
        return 0
    if roman_string is None:
        return 0
    for item in reversed(roman_string):
        for elem in digit:
            if item == elem[0]:
                if elem[1] < end:
                    outcome -= elem[1]
                else:
                    outcome += elem[1]
                end = elem[1]
    return outcome
