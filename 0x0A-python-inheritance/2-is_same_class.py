#!/usr/bin/python3
"""here you can find the function is_same_class"""


def is_same_class(obj, a_class):
    """function that returns true or false
        if the object is exactly an instance of the specified class"""
    if type(obj) is a_class:
        return True
    return False
