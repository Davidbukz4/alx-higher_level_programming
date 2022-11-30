#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 == 0:
        res = i
    else:
        res = i - 32
    print("{:s}".format(chr(res)), end="")
