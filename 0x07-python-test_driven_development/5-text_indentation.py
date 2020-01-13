#!/usr/bin/python3
"""5-text_indentation" is the module.

this module print a string is found ".", "?" or ":" 
follow by a new line and supplie a function text_indentation(text).
"""


def text_indentation(text):
    """print a string is found ".", "?" or ":" 
follow by a new line and supplie a function text_indentation(text)."""
    if type(text) is not str:
        raise TypeError("text must be a string")
    sentinel = 0
    for i in text:
        if sentinel == 0:
            if i == ' ':
                continue
            else:
                sentinel = 1
        if sentinel == 1:
            if i == '?' or i == '.' or i == ':':
                print(i)
                print()
                sentinel = 0
            else:
                print(i, end="")
