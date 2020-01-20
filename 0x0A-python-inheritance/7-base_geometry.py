#!/usr/bin/python3
"""here you can find the class BaseGeometry"""


class BaseGeometry():
    """here create the class"""
    def area(self):
        """Exception msg"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
