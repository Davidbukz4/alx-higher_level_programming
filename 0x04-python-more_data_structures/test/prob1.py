#!/usr/bin/python3

import random

randList = list(random.randint(1, 1001) for i in range(101))

mul_list = list(filter((lambda x: x % 9 == 0), randList))

print(mul_list)
