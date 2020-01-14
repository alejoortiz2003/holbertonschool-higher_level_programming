#!/usr/bin/python3
"""
This is the class rectangle
"""


class Rectangle:
    """creating a rectangle"""
    def __init__(self, width = 0, height = 0):
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
        """private instance height"""
        return self.__height

    @height.setter
    def height(self, value):
        """configuration for private attributes of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Function that print a rectangle filled with "#" """
        if self.area() == 0:
            return ""
        return '\n'.join(["#" * self.__width] * self.__height)

    def __repr__(self):
        """Function that return a replicate of rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)