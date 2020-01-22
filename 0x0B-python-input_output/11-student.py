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

    def to_json(self):
        """return the instance of the directory"""
        return self.__dict__
