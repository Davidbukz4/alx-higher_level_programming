#!/usr/bin/python3
"""
Defines a function that checks if an object inherited directly or
indirectly from a class
"""


def inherits_from(obj, a_class):
    """Returns true if object is an instance of a class it inherited
    from directly or indirectly
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
