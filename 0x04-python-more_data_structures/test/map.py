#!/usr/bin/python3

numList = range(1, 11)

def func(num):
    return num * 2

res = list(map(func, numList))
print(res)

print(list(map(lambda x: x * 5, numList)))

two_list = list(map(lambda x, y: x + y, [1,2,3], [6,5,4]))
print(two_list)
