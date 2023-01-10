#!/usr/bin/python3
"""
Defines a Rectangle class that inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A Rectangle class"""
    def __init__(self, width, height):
        """Initializes a class"""
        try:
            self.integer_validator('width', width)
            self.integer_validator('height', height)
            self.__width = width
            self.__height = height
        except Exception as e:
            raise e

    def area(self):
        """returns the area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """Returns the string representation of the class"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
