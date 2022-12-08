#!/usr/bin/python3
def weight_average(my_list=[]):
    if not len(my_list):
        return 0
    sum = 0
    denum = 0
    for i in range(len(my_list)):
        a, b = my_list[i]
        sum += (a * b)
        denum += b
    return sum / denum
