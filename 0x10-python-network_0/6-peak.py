#!/usr/bin/python3
"""function find_peak"""


def find_peak(list_unsorted):
    """finds a peak"""
    lu = list_unsorted
    l = len(lu)
    if l == 0:
        return
    m = l // 2
    if (m == l - 1 or lu[m] >= lu[m + 1]) and (m == 0 or lu[m] >= lu[m - 1]):
        return lu[m]
    if m != l - 1 and lu[m + 1] > lu[m]:
        return find_peak(lu[m + 1:])
    return find_peak(lu[:m])
