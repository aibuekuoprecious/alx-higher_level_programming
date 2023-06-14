#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [list(map(lambda element: element * element, row)) for row in matrix]
