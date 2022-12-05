#!/usr/bin/python3

def max_integer(my_list=[]):
    if not len(my_list):
        return None
    temp = my_list[0]
    for j in range(1, len(my_list)):
        if temp < my_list[j]:
            temp = my_list[j]
    return temp
