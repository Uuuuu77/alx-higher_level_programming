#!/usr/bin/python3
"""
   This is Matrix Division
"""


def matrix_divided(matrix, div):
    """
      Each Element is divided in the matrix by an integer/float
    """
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    len0 = len(matrix[0]) if matrix else None

    if not len0:
        raise TypeError(err_msg)
    if all(len(m_row) == len0 for m_row in matrix) is False:
        raise TypeError("Each row of the matrix must have the same size")
    if all(isinstance(m_row, list) for m_row in matrix) is False:
        raise TypeError(err_msg)
    if all(isinstance(a, (int, float)) for b in matrix for a in b) is False:
        raise TypeError(err_msg)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]
