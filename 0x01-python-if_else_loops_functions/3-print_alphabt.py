#!/usr/bin/python3
for i in range(ord('a'), ord('z')+1):
	if chr(i) is 'e' or chr(i) is 'q':
	    continue
	print("{:c}".format(i), end="")
