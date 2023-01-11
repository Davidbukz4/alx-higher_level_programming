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
        return self.__dict__
