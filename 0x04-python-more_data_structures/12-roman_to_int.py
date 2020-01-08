#!/usr/bin/python3
def roman_to_int(roman_string):
    cr = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    value = 0
    if roman_string is not None or roman_string is str:
        for i in range(len(roman_string)):
            if i > 1:
                if (cr[roman_string[i - 1]] <= cr[roman_string[i]]):
                    value += cr[i]
                    return value
                else:
                    value += cr[i]
                return value -2
    else:
        return 0
