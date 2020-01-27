#!/usr/bin/python3
"""
here you can find the class Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """here start the class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """function for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter of size"""
        self.width = value
        self.height = value

    def __str__(self):
        """function __str___"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.__size)

    def update(self, *args, **kwargs):
        """function update"""
        if args:
            for i, value in enumerate(args):
                if i == 0:
                    self.id = value
                elif i == 1:
                    self.__size = value
                elif i == 2:
                    self.x = value
                elif i == 3:
                    self.y = value
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

        def to_dictionary(self):
            """function to_dictionary"""
            dic = {}
            dic["id"] = self.id
            dic["size"] = self.size
            dic["x"] = self.x
            dic["y"] = self.y
            return dic
