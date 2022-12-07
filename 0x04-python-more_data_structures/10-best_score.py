#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary is {}:
        return None
    highest_value = max(a_dictionary.values())
    for key, value in a_dictionary.items():
        if a_dictionary.get(key) == highest_value:
            return key
