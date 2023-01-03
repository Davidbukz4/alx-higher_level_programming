#!/usr/bin/python3
"""

This module prints a text with 2 new lines after each of these characters
., ? and :
"""


def text_indentation(text):
    """This function prints a text with 2 new lines
        after each of these characters: ., ? and :
    Args:
        text: string of characters
    Raises:
        TypeError: text must be a string
    Returns:
        nothing
    """
    if not isinstance(text, str) or text is None:
        raise TypeError('text must be a string')
    str1 = "".join([ch if ch not in ".?:" else ch + "\n\n" for ch in text])
    print("\n".join([line.strip() for line in str1.split("\n")]), end="")
