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
            obj = [x.to_dictionary() for x in list_objs]
        obj = cls.to_json_string(obj)
        fn = cls.__name__+".json"
        with open(fn, "w") as file:
            file.write(obj)

    def from_json_string(json_string):
        """function from_json_string"""
        ls = []
        if json_string is None:
            return ls
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """function create"""
        if cls.__name__ == "Rectangle":
            dummy = cls(2, 3)
            dummy.update(**dictionary)
            return dummy
        if cls.__name__ == "Square":
            dummy = cls(5)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """function load_from_file"""
        filename = cls.__name__ + ".json"
        file = []
        try:
            with open(filename, 'r') as f:
                file = cls.from_json_string(f.read())
            for i, value in enumerate(file):
                file[i] = cls.create(**file[i])
        except:
            pass
        return file
