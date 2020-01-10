#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        return (self.__size) ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(selft, value):
        if type(value) is not tuple or len(value) != 2 \
           or type(value[0]) is not int or value[0] < 0 \
           or type(value[1]) is not int or value[1] <0:
            raise TypeError("poisition must be a tuple of 2 positive integer")
        else:
            self.__position = value
