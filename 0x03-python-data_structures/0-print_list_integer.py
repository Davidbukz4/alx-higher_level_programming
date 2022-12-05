#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if not len(my_list):
        return
    for x in range(0, len(my_list)):
        print("{:d}".format(my_list[x]))
