#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return [list(map((lambda x, y: x ** 2), matrix[y], range(len(matrix))))]
