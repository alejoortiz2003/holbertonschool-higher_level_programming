#!/usr/bin/python3
"""
This is the class rectangle
"""


class Rectangle:
    """creating a rectangle"""
    def __init__(self, width = 0, heigth = 0):
        """init the rectangle"""
        self.width = width
        self.heigth = heigth
    
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
    def heigth(self):
        """private instance heigth"""
        return self.__heigth

    @heigth.setter
    def heigth(self, value):
        """configuration for private attributes of heigth"""
        if type(value) is not int:
            raise TypeError("heigth must be an integer")
        if value < 0:
            raise ValueError("heigth must be >= 0")
        self.__heigth = value