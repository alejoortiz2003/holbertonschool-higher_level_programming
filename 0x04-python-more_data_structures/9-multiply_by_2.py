#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for i in new_dict:
        new_dict[i] = new_dict[i] + new_dict[i]
    return new_dict
