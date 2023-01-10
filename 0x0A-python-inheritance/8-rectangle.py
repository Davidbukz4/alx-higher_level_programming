#!/usr/bin/python3
"""
Defines a Rectangle class that inherits from BaseGeometry
"""


class BaseGeometry:
    """A BaseGeometry class"""
    def __init__(self, width, height):
        """Initializes the class"""
        pass

    def area(self):
        """checks if area method is implemented"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates a value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A Rectangle class"""
    def __init__(self, width, height):
        """initializes a class"""
        try:
            self.integer_validator('width', width)
            self.integer_validator('height', height)
            self.__width = width
            self.__height = height
        except Exception as e:
            raise e
