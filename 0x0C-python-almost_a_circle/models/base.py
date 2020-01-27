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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Function save_to_file"""
        obj = []
        if list_objs is None:
            obj = []
        else:
            obj = [x.to_dictionary() for i in list_objs]
        obj = cls.to_json_string(obj)
        fn = cls.__name__+".json"
        with open(fn, "w") as file:
            file.write(obj)
