#!/usr/bin/python3
"""
Divide a matrix
matrix must be a list of lists of integers or floats
Each row of the matrix must have the same size with up to 2 decimal places
"""


def matrix_divided(matrix, div):
    """
    Returns new matrix list of lists with dividends
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    errorMessage = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(errorMessage)

    new_matrix = []
    samelen = len(matrix[0])
    for lists in matrix:
        if type(lists) is not list:
            raise TypeError(errorMessage)
        if len(lists) != samelen:
            raise TypeError("Each row of the matrix must have the same size")
        newlist = []
        for i in lists:
            if not isinstance(i, (int, float)):
                raise TypeError(errorMessage)
            newlist.append(round(i/div, 2))
        new_matrix.append(newlist)
    return new_matrix
