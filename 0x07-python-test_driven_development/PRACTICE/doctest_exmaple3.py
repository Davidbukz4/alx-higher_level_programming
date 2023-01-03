#!/usr/bin/python3

def double_space(lines):
    """Prints a list of lines
    >>> double_space(['line one.', 'line two.'])
    line one.
    <BLANKLINE>
    line two.
    <BLANKLINE>
    """
    for l in lines:
        print(l)
        print()
