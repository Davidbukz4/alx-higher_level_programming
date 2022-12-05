#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print("{:s}".format(""))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print("{:d}".format(matrix[i][j]), end=" ")
        print("")
