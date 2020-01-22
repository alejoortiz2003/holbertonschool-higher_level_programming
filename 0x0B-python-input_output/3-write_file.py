#!/usr/bin/python3
"""
here we can find the write_file function
"""


def write_file(filename="", text=""):
    """function that returns the numbers of character written"""
    with open(filename, "w", encoding='UTF-8') as a_file:
        return (a_file.write(text))
