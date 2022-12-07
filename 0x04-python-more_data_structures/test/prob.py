#!/usr/bin/python3

import random

HT_list = []

HT_list = [random.choice(['H', 'T']) for i in range(1,101)]

print('H\'s: ', HT_list.count('H'))
print('T\'s: ', HT_list.count('T'))
