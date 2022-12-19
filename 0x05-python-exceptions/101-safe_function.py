#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        a, b = args
        res = fct(a, b)
    except Exception as err:
        sys.stderr.write("Exception: {}\n".format(err))
        res = None
    return res
