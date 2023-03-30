#!/usr/bin/python3
""" Finds a peak """

def find_peak(list_of_integers):
    """ This function finds a peak in a list of integers"""
    if not list_of_integers:
        return
    temp = list_of_integers[0]
    for i in range(1, len(list_of_integers)):
        if temp < list_of_integers[i]:
            temp = list_of_integers[i]
    return temp
