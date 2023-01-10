#!/usr/bin/python3
"""
Defines a BaseGeometry class that inherits from Rectangle class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Square class"""
    def __init__(self, size):
        """initializes the class"""
        try:
            self.integer_validator("size", size)
            self.__size = size
            super().__init__(size, size)
        except Exception as e:
            raise e

    def area(self):
        """returns the area of the square"""
        return (super().area())
