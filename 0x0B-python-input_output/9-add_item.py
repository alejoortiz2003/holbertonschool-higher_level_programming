#!/usr/bin/python3
"""
script that adds arguments
"""


from sys import argv


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    f_json = load_from_json_file(filename)
except:
    f_json = []

for i in argv[:1]:
    f_json.append(i)

save_to_json_file(f_json, filename)
