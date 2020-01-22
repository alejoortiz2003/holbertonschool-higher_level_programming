#!/usr/bin/python3
"""
here we can find the from_json_string function
"""


import json


def load_from_json_file(filename):
    """function that return the string representation of an object"""
    with open(filename, mode="w", encoding='utf-8') as a_file:
        return (json.load(a_file))
