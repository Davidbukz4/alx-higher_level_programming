#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div

arg_len = len(sys.argv) - 1
if arg_len != 3:
    print("{:s}".format("Usage: ./100-my_calculator.py <a> <operator> <b>"))
    exit(1)
operator = "+-*/"

a = int(sys.argv[1])
b = int(sys.argv[3])

if sys.argv[2] not in operator:
    error = "Unknown operator. Available operators: +, -, * and /"
    print("{:s}".format(error))
    exit(1)
if sys.argv[2] in operator:
    if sys.argv[2] == operator[0]:
        formula = add
    elif sys.argv[2] == operator[1]:
        formula = sub
    elif sys.argv[2] == operator[2]:
        formula = mul
    else:
        formula = div

print("{:d} {:s} {:d} = {:d}".format(a, sys.argv[2], b, formula(a, b)))
