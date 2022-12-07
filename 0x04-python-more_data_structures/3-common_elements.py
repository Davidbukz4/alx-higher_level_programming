#!/usr/bin/python3

def common_elements(set_1, set_2):
    if not set_1 or not set_2:
        return []
    new_list = set()
# & can also be used for intersection
    new_list = set_1.intersection(set_2)
    return new_list
