#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        print_status = True
    except ValueError:
        print_status = False
    except Exception:
        print_status = False
    return print_status
