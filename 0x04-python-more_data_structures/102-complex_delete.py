#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not a_dictionary or value is None:
        return {}
    del_list = []
    for key, val in a_dictionary.items():
        if a_dictionary.get(key) == value:
            del_list.append(key)
    for i in range(len(del_list)):
        del a_dictionary[del_list[i]]
    return a_dictionary
