#!/usr/bin/python3

def this_raise():
    """This function always returns an exception
    >>> this_raises()
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        File "<stdin>", line 2, in this_raises
    RuntimeError: here is the error
    """
    raise RuntimeError('here is the error')
 
