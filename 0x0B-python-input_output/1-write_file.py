#!/usr/bin/python3
"""
Defines a function that writes to a text file
"""


def write_file(filename="", text=""):
    """Writes a string to a text file
    Arg:
        filename (str): name of file to save string to
        text (str): text to write
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        no_of_char = f.write(text)
    return (no_of_char)
