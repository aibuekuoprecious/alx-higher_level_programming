#!/usr/bin/python3
"""
    101-lazy_matrix_mul Module
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices

    Args:
        m_a: first matrix(2D List)
        m_b: second matrix(2D List)

    Returns:
        the product of two matrices
    """
    if not all(isinstance(i, list) for i in [m_a, m_b]):
        raise TypeError("m_a and m_b must be a list")
    if not all(m_a) or not all(m_b):
        raise ValueError("m_a and m_b can't be empty")
    for blocks in [m_a, m_b]:
        if not all(isinstance(i, list) for i in blocks):
            raise TypeError(f"{blocks} must be a list of lists")
        if not all(blocks):
            raise ValueError(f"{blocks} can't be empty")
        for integers in blocks:
            if not all(isinstance(i, (int, float)) for i in integers):
                raise TypeError(f"{blocks} contains only integers or floats")
        if len(set(map(len, blocks))) > 1:
            raise TypeError(f"each row of {blocks} must be of the same size")

    if len(m_a[0]) != len(m_b):  # cols of m_a must be equal to rows of m_b
        raise ValueError("m_a and m_b can't be multiplied")

    return np.matmul(m_a, m_b)
