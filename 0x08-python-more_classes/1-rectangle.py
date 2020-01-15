#!/usr/bin/python3
"""
This is the class rectangle
"""


class Rectangle:
    """creating a rectangle"""
    def __init__(self, width=0, height=0):
        """init the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """private instance width"""
        return self.__width

    @width.setter
    def width(self, value):
        """configuration for private attributes of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """private instance heigth"""
        return self.__height

    @heigth.setter
    def height(self, value):
        """configuration for private attributes of heigth"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
