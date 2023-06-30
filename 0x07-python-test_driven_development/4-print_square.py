#!/usr/bin/python3
"""
    4-print_square Module
"""


def print_square(size):
    """
        Prints a square with the character '#'

        Args:
            size: size length of the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    square = ('#' * size + '\n') * size
    print(square, end='')
