#!/usr/bin/python3
"""4-print_square" is the module.

this module print a string and supplie a function print_square(size).
"""


def print_square(size):
    """print a square filled by "#" and the size is a variable call size"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size is float and size < 0:
        raise TypeError("size must be an integer")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
