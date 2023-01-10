#!/usr/bin/python3
"""
Defines a function that adds attribute to an object
"""


def add_attribute(obj, attr, value):
    """Adds a new attribute to an object if possible
    Args:
        obj (any): the object to add an attribute to
        attr (str): the name of attribute to add to object
        value (any): the value of attribute
    Raises:
        TypeError: can't add new attribute
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr, value)
