#!/usr/bin/python3
"""function find_peak"""


def find_peak(list_unsorted):
    """finds a peak"""
    l_u = list_unsorted
    l = len(l_u)
    if l == 0:
        return
    m = l // 2
    if (m == l - 1 or l_u[m] >= l_u[m + 1]) and (m == 0 or l_u[m] >= l_u[m - 1]):
        return l_u[m]
    if m != l - 1 and l_u[m + 1] > l_u[m]:
        return find_peak(l_u[m + 1:])
    return find_peak(l_u[:m])
