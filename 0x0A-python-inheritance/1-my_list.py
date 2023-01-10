#!/usr/bin/python3
"""
A module that inherits from list (class)
"""


class MyList(list):
    """This class inherits from list"""
    def print_sorted(self):
        """This function prints a list but sorted(ascending sort)"""
        new_list = self[:]
        new_list.sort()
        print(new_list)
