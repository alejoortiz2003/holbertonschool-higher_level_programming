#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not (len(matrix) == 1 and len(matrix[0]) == 0):
        for i in matrix:
            for j, element in enumerate(i):
                if (j + 1) != len(i):
                    print("{:d} ".format(element), end="")
                else:
                    print("{:d}".format(element))
    else:
        print("")
