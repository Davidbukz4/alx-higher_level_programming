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
                * height must be an integer
        ValueError:
                * width must be >= 0
                * height must be >= 0
    Returns:
        * area
        * perimeter
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """It initializes an instance of the class"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Retrieves the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return (self.height * self.width)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (2*(self.height + self.width))

    def __str__(self):
        """Returns the printable representation of the rectangle
        Represent the rectangle with '#'
        """
        if self.width == 0 or self.height == 0:
            return ("")
        else:
            str_rep = []
            sym = str(self.print_symbol)
            for i in range(self.height):
                [str_rep.append(sym) for j in range(self.width)]
                if i != self.height - 1:
                    str_rep.append('\n')
            return ("".join(str_rep))

    def __repr__(self):
        """Returns the string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Called when a instance is about to be destroyed"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
