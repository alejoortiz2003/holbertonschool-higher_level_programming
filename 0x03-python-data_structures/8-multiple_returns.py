#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) is 0:
        my_t = (len(sentence), None)
    else:
        my_t = (len(sentence), sentence[0])
    return my_t
