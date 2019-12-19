#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[row * row for row in i] for i in matrix[:]]
