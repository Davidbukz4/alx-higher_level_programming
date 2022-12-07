#!/usr/bin/python3

def mult_by_2(num):
    return num * 2

def do_math(func, num):
    return func(num)

print('8 * 2=', do_math(mult_by_2, 8))
