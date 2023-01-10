#!/usr/bin/python3
"""
Defines a function that reads a text file
"""


def read_file(filename=""):
    """Reads a text file
    Arg:
        filename (str): name of text file to be opened
    """
    with open(filename, encoding="utf-8") as f:
        data = f.read()
        print(data, end="")
