#!/usr/bin/python3
"""Module to divide a matrix list"""


def matrix_divided(matrix, div):
    """Method to divide the matric list.
    Must check if matrix is a list of integers or floats
    Each row of the matrix must also be same size
    The div variable must be an integer or float
    div also cannot be equal to 0
    All elements of matrix be divided by div
    Returns a new matrix
    """
    if not all(isinstance(elements, list) for elements in matrix:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    else:
        if not all(isinstance(elements, (int, float)) for elements in matrix:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
