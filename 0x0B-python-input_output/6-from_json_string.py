#!/usr/bin/python3
"""
here we can find the from_json_string function
"""


import json


def from_json_string(my_str):
    """function that return the string representation of an object"""
    return (json.loads(my_str))
