#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not len(my_list):
        return
    for x in reversed(my_list):
        print("{:d}".format(x))
