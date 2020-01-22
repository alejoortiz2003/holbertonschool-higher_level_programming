#!/usr/bin/python3
"""
here we can find the from_json_string function
"""


import json


def save_to_json_file(my_obj, filename):
    """function that return the string representation of an object"""
    with open(filename, mode="w", encoding='utf-8') as a_file:
        return (json.dump(my_obj, a_file))
