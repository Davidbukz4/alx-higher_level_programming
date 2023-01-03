#!/usr/bin/python3


def func(a,b):
    """Returns a * b.

    >>> func(['A', 'B'], 3) #doctest: +NORMALIZE_WHITESPACE
    ['A', 'B',
    'A', 'B',
    'A', 'B']
    >>> func(2, 3) #doctest: +REPORT_NDIFF
    6 
     """
    return a * b

