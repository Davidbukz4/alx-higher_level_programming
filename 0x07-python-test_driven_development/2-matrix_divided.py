#!/usr/bin/python3
"""

    This module divides a matrix

"""


def matrix_divided(matrix, div):
    """This function divides all elements of a matrix
    Args:
        matrix: a matrix
        div: a value to divide element with
    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size
        TypeError: div must be a number
        ZeroDivisionError: division by zero
    Returns:
        new matrix with elements divided by div
    """
    if not isinstance(matrix, list) or not matrix:
        raise TypeError('matrix must be a \
matrix (list of lists) of integers/floats')
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError('matrix must be a \
matrix (list of lists) of integers/floats')
    for row in matrix:
        if len(matrix[0]) != len(row):
            raise TypeError('Each row of the matrix must have the same size')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0 or round(div, 2) == 0:
        raise ZeroDivisionError('division by zero')

    n = list(map((lambda i: list(map((lambda x: round(x/div, 2)), i))), matrix))

    return n
