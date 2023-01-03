#!/usr/bin/python3
"""

    A function that adds 2 integers

"""


def add_integer(a, b=98):
    """Adds two integers
    Args:
        a: integer or float value
        b: integer or float value
    Raises:
        TypeError: a must be an integer
        TypeError: b must be an integer
    Returns:
        addition of two number
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
