#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
    except ZeroDivisionError as err:
        sys.stderr.write("Exception: {}\n".format(err))
        res = None
    except IndexError as err:
        sys.stderr.write("Exception: {}\n".format(err))
        res = None
    except Exception as err:
        sys.stderr.write("Exception: {}\n".format(err))
        res = None
    return res
