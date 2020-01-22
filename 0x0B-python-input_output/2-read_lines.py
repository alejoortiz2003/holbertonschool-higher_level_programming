#!/usr/bin/python3
"""
here we can find the read_file function
"""


def read_lines(filename="", nb_lines=0):
    """reads a file and return the number of lines"""
    with open(filename, "r", encoding='UTF-8') as a_file:
        if nb_lines <= 0:
            print(a_file.read(), end="")
            return
        cnol = 0
        for cnol, line in enumerate(a_file):
            if cnol == nb_lines:
                break
            print(line, end="")
