#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        maxn = max(a_dictionary.values())
        return [i for i, idx in a_dictionary.items() if idx == maxn][0]
