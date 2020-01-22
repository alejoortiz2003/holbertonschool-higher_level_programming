#!/usr/bin/python3
"""
here we can find the append_write function
"""


def append_write(filename="", text=""):
    """function that append"""
    with open(filename, "a", encoding='UTF-8') as a_file:
        return (a_file.write(text))
