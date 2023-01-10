#!/usr/bin/python3
"""
Defines a function that checks if an object is exactly an instance
of the specified class
"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance
    of the specified class
    Args:
        obj (any): the object to check
        a_class (type): the class to compare the type of obj to
    """
    if type(obj) == a_class:
        return True
    else:
        return False
