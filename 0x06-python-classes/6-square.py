#!/usr/bin/python3
"""This module contains a class that defines a square"""


class Square():
    """Defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new square
        Args:
            size (int): size of square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrieves the size of the square"""
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

    @property
    def position(self):
        """Retrieves the poistion of the square"""
        return self.__position

    @position.setter
    def position(self, position):
        """Sets the position"""
        if isinstance(position, tuple) and len(position) == 2:
            if position[0] >= 0 and position[1] >= 0:
                self.__position = position
            else:
                raise TypeError('position must be a tuple of 2 positive integers')
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                if (self.__position[1] > 0):
                    print("")
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    print("{}".format('#'), end="")
                print("")
