#!/usr/bin/python3
"""
here you can find the class Base
"""


import json


class Base:
    """here start the class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """here start the function to_json_string"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)
