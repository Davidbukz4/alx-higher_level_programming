#!/usr/bin/python3
"""
Defines a BaseGeometry module
"""


class BaseGeometry:
    """A BaseGeometry class"""
    def __init__(self):
        """initializes the class"""
        pass

    def area(self):
        """checks if area is implemented"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
