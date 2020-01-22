#!/usr/bin/python3
"""
Here you can find the class "Student"
"""


class Student:
    """Here init the class"""
    def __init__(self, first_name, last_name, age):
        """here init the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return the instance of the directory"""
        if attrs is None:
            return self.__dict__
        _dict = {}
        for i in attrs:
            try:
                _dict[i] = self.__dict__[i]
            except:
                pass
        return _dict

    def reload_from_json(self, json):
        """replaces attributes from the Student instance"""
        for key in json:
            try:
                setattr(self, key, json[key])
            except:
                pass
