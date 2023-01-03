#!/usr/bin/python3
"""
This module defines a rectangle
"""


class Rectangle:
    """This function returns the area of a rectangle
    Args:
        width: width of the rectangle
        height: height of the rectangle
    Raises:
        TypeError:
                * width must be an integer
    """
    def __init__(self, width=0, height=0):
        """It initializes an instance of the class"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        """Sets the width"""
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    @property
    def height(self):
        """Retrieves the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        """Sets the height of the rectangle"""
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height
