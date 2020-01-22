#!/usr/bin/python3
"""
here we can find the number_of_lines function
"""


def number_of_lines(filename=""):
    """reads a file and return the number of lines"""
    with open(filename, "r", encoding='UTF-8') as a_file:
        nol = 0
        for line in a_file:
            nol += 1
        return nol
