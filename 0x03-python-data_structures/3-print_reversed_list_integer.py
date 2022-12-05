#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not len(my_list):
        return my_list
    for x in range(-1, -len(my_list) - 1, -1):
        print(my_list[x])
