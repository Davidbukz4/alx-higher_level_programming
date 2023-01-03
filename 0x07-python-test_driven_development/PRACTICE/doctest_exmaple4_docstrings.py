#!/usr/bin/python3

"""Tests can appear in any docstring within module
>>> A('a') == B('b')
False
"""

class A:
    """Simple class
    >>> A('instance_name').name
    'instance_name'
    """
    def __init__(self, name):
        self.name = name
    def method(self):
        """Returns an unusal value
        >>> A('name').method()
        'eman'
        """
        return ''.join(reversed(self.name))

class B(A):
    """Another class
    >>> B('different_name').name
    'different_name'
    """
