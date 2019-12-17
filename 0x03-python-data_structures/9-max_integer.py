#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == "":
        return None
    c = 0
    for i in my_list:
        if i > c:
            c = i
    return c
