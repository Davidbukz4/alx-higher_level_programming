#!/usr/bin/python3
"""This module contains a class that defines a square"""


class Square():
    """Defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new square
        Args:
            size (int): size of square
        """
        self.size = size
        self.position = position

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
        flag = 0
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(position) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            for i in position:
                if not isinstance(i, int):
                    flag = 1
                    raise TypeError("position must be a tuple\
 of 2 positive integers")
                elif i < 0:
                    flag = 1
                    raise TypeError("position must be a tuple\
 of 2 positive integers")
            if flag == 0:
                self.__position = position

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.size == 0:
            print("")
        else:
            a = self.position[1]
            while (a > 0):
                print("")
                a -= 1
            for i in range(self.size):
                b = self.position[0]
                for k in range(self.size):
                    while (b > 0):
                        print(" ", end="")
                        b -= 1
                    print("{}".format('#'), end="")
                print("")

    def __str__(self):
        """This method has the same behavior  as my_print()"""
        word = ""
        if (self.size == 0):
            return (word)
        else:
            a = self.position[1]
            while (a > 0):
                word = word + "\n"
                a -= 1
            for i in range(self.size):
                b = self.position[0]
                for j in range(self.size):
                    while(b > 0):
                        word += " "
                        b -= 1
                    word += "#"
                if (i < self.size - 1):
                    word += "\n"
            return word
