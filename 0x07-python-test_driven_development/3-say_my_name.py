#!/usr/bin/python3
"""

This module prints the first name and last name

"""


def say_my_name(first_name, last_name=""):
    """This function prints 'My name is <first name> <last name>
    Args:
        first_name: first name in strings
        last_name: last name in strings
    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string
    Returns:
        void
    """
    if not isinstance(first_name, str) or first_name is None:
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str) or last_name is None:
        raise TypeError('last_name must be a string')
    print("My name is {:s} {:s}".format(first_name, last_name))
