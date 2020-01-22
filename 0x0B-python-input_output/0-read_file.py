#!/usr/bin/python3
"""
here we can find the read_file function
"""


def read_file(filename=""):
    """reads a file and prints"""
    with open(filename, "r", encoding='UTF-8') as a_file:
        print(a_file.read(), end="")
