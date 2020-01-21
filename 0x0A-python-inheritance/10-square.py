#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""here you can find the class BaseGeometry"""


class Square(Rectangle):
    """here create the class"""
    def __init__(self, size):
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

