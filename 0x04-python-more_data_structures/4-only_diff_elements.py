#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    if not set_1 or not set_2:
        return []
    new_set = set()
    new_set = set_1 ^ set_2
    return new_set
