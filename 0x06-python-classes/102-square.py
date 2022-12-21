#!/usr/bin/python3
"""This module contains a class that defines a square"""


class Square():
    """Defines a square"""
    def __init__(self, size=0):
        """Initializes a new square
        Args:
            size (int): size of square
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size"""
        return self.__size

    @size.setter
    def size(self, size):
        """Sets the size"""
        if isinstance(size, int) and size >= 0:
            self.__size = size
        elif not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif (size < 0):
            raise ValueError('size must be >= 0')

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    def __lt__(self, other):
        """True if self is less than other, False otherwise"""
        return self.size < other.size

    def __le__(self, other):
        """True if self is less than or equal to other, False otherwise"""
        return self.size <= other.size

    def __eq__(self, other):
        """True if self is equal to other, False otherwise"""
        return self.size == other.size

    def __ne__(self, other):
        """True if self is not equal to other, False otherwise"""
        return self.size != other.size

    def __gt__(self, other):
        """True if self is greater than other, False otherwise"""
        return self.size > other.size

    def __ge__(self, other):
        """True if self is greater than or equal to other, False otherwise"""
        return self.size >= other.size
