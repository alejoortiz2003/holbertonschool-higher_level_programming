#!/usr/bin/python3
"""here you can find the function pritn_sorted"""


class MyList(list):
    """"""
    def __init__(self):
        """here create a subclass"""
        super().__init__()

    def print_sorted(self):
        """here we can print the sorted list"""
        print(sorted(self))
