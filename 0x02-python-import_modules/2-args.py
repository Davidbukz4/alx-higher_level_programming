#!/usr/bin/python3

if __name__ == '__main__':
    import sys
arg_len = len(sys.argv)
arg_len -= 1
if arg_len == 0:
    argNum = "arguments."
elif arg_len == 1:
    argNum = "argument:"
else:
    argNum = "arguments:"

print("{:d} {:s}".format(arg_len, argNum))

for i in range(1, len(sys.argv)):
    print('{:d}{:s} {:s}'.format(i, ":", sys.argv[i]))
