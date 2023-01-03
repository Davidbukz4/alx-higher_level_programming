#!/usr/bin/python3
"""

This module print square

"""


def print_square(size):
    """This function prints a square with the character #
    Args:
        size: size length of the square
    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    Returns:
        nothings
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if isinstance(size, int) and size < 0:
        raise ValueError('size must be >= 0')
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    for i in range(size):
        print("#" * size)
