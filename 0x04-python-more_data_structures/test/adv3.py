#!/usr/bin/python3

def is_it_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True

def change_list(list, func):
    oddList = []
    oddList = [i for i in list if func(i)]
    return oddList

aList = range(1, 20)
print(change_list(aList, is_it_odd))
