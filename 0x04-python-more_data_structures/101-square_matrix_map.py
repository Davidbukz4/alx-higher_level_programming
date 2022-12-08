#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map((lambda list_2d: list(map((lambda x: x ** 2), list_2d))), matrix))
