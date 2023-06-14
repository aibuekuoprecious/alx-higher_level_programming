#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [list(map(lambda elem: elem * elem, row)) for row in matrix]
