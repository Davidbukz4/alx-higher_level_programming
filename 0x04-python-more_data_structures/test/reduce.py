#!/usr/bin/python3

from functools import reduce

print(reduce((lambda x, y: x + y), range(1,6)))
