#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        print_status = True
    except ValueError as err:
        sys.stderr.write("Exception: {}\n".format(err))
        print_status = False
    except Exception as err:
        sys.stderr.write("Exception: {}\n".format(err))
        print_status = False
    return print_status
