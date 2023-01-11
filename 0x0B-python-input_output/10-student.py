#!/usr/bin/python3
"""
Student to JSON
"""


class Student:
    """A student class"""
    def __init__(self, first_name, last_name, age):
        """Initializes the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a student instance"""
        if type(attrs) is not list:
            return self.__dict__
        else:
            new = {}
            obj = self.__dict__
            for i in attrs:
                for elem in obj:
                    if (i == elem):
                        new[i] = obj[i]
            return new
