#!/usr/bin/python3
"""
This is a lockedClass module
"""


class LockedClass():
    """prevents the user from dynamically creating new instance attributes"""
    __slots__ = ['first_name']
    def __inti__(self):
        pass
