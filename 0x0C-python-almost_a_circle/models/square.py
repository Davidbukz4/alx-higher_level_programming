#!/usr/bin/python3
"""
Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the square class"""
        super().__init__(size, size, x, y, id)
        self.width = size
        self.height = size

    @property
    def size(self):
        """Returns the size(width or height) of the square"""
        return self.width

    @size.setter
    def size(self, size):
        """Sets the size(width and height) for the square"""
        self.width = size
        self.height = size

    def __str__(self):
        """Returns a printable representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,\
                self.y, self.width)

    def update(self, *args, **kwargs):
        """Assigns key/value argument to attributes"""
        i = 0
        for arg in args:
            if i == 0:
                self.id = arg
            elif i == 1:
                self.size = arg
            elif i == 2:
                self.x = arg
            elif i == 3:
                self.y = arg
            else:
                break
            i += 1

        if not(args):
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the square"""
        dic = {}
        for key, value in self.__dict__.items():
            key = key.split('__')
            key = key[-1]
            if key == 'width' or key == 'height':
                key = 'size'
            dic.update({key:value})
        return dic
