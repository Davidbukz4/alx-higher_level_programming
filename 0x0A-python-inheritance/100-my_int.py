#!/usr/bin/python3
"""
Defines a class MyInt that inherits from int class
"""


class MyInt(int):
    """MyInt class"""
    def __init__(self, size):
        """initializes the class"""
        self.__size = size

    def __eq__(self, other):
        """returns not equal to comparison"""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """returns equal to comparison"""
        return int.__eq__(self, other)
