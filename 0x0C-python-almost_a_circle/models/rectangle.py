#!/usr/bin/python3
"""
First Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """A Rectangle class that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the Rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Retrieves width attribute"""
        return self.__width

    @width.setter
    def width(self, width):
        """Sets the width attributes"""
        if not(type(width) == int):
            raise TypeError('width must be an integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = width

    @property
    def height(self):
        """Retrieves height attribute"""
        return self.__height

    @height.setter
    def height(self, height):
        """Sets the height attribute"""
        if not(type(height) == int):
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = height

    @property
    def x(self):
        """Retrieves the x attribute"""
        return self.__x

    @x.setter
    def x(self, x):
        """Sets the x attribute"""
        if not(type(x) == int):
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = x

    @property
    def y(self):
        """Retrieves the y attribute"""
        return self.__y

    @y.setter
    def y(self, y):
        """Sets the y attribute"""
        if not(type(y) == int):
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = y

    def area(self):
        """Returns the area of the rectangle instance"""
        return (self.width * self.height)

    def display(self):
        """Prints in stdout the Rectangle instance with the # character"""
        status = 1
        for y in range(self.y):
            print()
        for h in range(self.height):
            for w in range(self.width):
                if status:
                    for x in range(self.x):
                        print(end=" ")
                print('#', end="")
                status = 0
            print()
            status = 1

    def __str__(self):
        """Returns printable string for the class"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,\
                self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Assigns a key/value argument to each attribute"""
        i = 1
        for arg in args:
            if i == 1:
                self.id = arg
            elif i == 2:
                self.width = arg
            elif i == 3:
                self.height = arg
            elif i == 4:
                self.x = arg
            elif i == 5:
                self.y = arg
            else:
                break
            i += 1
        if not(args):
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the Rectangle"""
        dic = {}
        for key, value in self.__dict__.items():
            key = key.split('__')
            key = key[-1]
            dic.update({key:value})
        return dic
