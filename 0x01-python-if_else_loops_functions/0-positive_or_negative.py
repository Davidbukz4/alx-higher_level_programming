#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("{:d}".format(number), f"{'is positive'}")
elif number == 0:
    print("{:d}".format(number), f"{'is zero'}")
else:
    print("{:d}".format(number), f"{'is negative'}")
