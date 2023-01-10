#!/usr/bin/python3
"""
Defines a function that checks if the object is an instance of,
or if the object is an instance of a class that inherited from
specified class
"""


def is_kind_of_class(obj, a_class):
    """Returns true if object is an instance of
    or object is an instance of class it inherited from
    specified class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
