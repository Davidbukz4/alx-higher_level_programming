#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    # my_list.copy() can also be used
    list_copy = my_list[:]
    if idx < 0:
        return list_copy
    if idx >= len(my_list):
        return list_copy
    list_copy[idx] = element
    return list_copy
