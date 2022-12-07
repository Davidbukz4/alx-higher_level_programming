#!/usr/bin/python3

def uniq_add(my_list=[]):
    if my_list is None:
        return None
    uniq_list = set(my_list)
    sum = 0
    for value in uniq_list:
        sum += value
    return sum
