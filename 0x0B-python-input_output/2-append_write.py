#!/usr/bin/python3
"""
Defines a function that appends a string and returns the no of
character appended
"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file
    and returns the number of character appended
    Args:
        filename (str): name of text file
        text (str): text to append
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        no_of_char = f.write(text)
    return no_of_char
