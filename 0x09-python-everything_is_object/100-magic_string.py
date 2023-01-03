#!/usr/bin/python3
def magic_string(my_list=[]):
    my_list += [1]
    return (("BestSchool, " * (len(my_list) - 1)) + "BestSchool")
