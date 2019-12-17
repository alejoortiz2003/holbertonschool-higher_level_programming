#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) is 0:
        sentence[0] = None
    length = len(sentence)
    return ((length, sentence[0]))
