#!/usr/bin/python3
"""
This module returns the multiplication two matrices
with 
"""


def matrix_mul(m_a, m_b):
    """This function multiplies two matrices
    Args:
        m_a: matrix A
        m_b: matrix B
    Raises:
        TypeError:
                * m_a must be a list
                * m_b must be a list
                * m_a must be a list of lists
                * m_b must be a list of lists
                * m_a should contain only integers or floats
                * m_b should contain only integers or floats
                * each row of m_a must be of the same size
                * each row of m_b must be of the same size
        ValueError:
                * m_a can't be empty
                * m_b can't be empty
                * m_a and m_b can't be multiplied
        Returns: new matrix which is the product of m_a and m_b
    """
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    for i in range(len(m_a)):
        if not isinstance(m_a[i], list):
            raise TypeError('m_a must be a list of lists')
    for i in range(len(m_b)):
        if not isinstance(m_b[i], list):
            raise TypeError('m_b must be a list of lists')
    if m_a == [] or m_a == [[]]:
        raise ValueError('m_a can\'t be empty')
    if m_b == [] or m_b == [[]]:
        raise ValueError('m_b can\'t be empty')
    for i in m_a:
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError('m_a should contain only integers or floats')
    for i in m_b:
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError('m_b should contain only integers or floats')
    for i in range(1, len(m_a)):
        if len(m_a[0]) != len(m_a[i]):
            raise TypeError('each row of m_a must be of the same size')
    for i in range(1, len(m_b)):
        if len(m_b[0]) != len(m_b[i]):
            raise TypeError('each row of m_b must be of the same size')
    if len(m_a[0]) != len(m_b):
        raise ValueError('m_a and m_b can\'t be multiplied')


    res = []
    row = []
    temp = 0
    for i in range(len(m_a)):
        for j in  range(len(m_b[0])):
            for k in range(len(m_b)):
                mul = (m_a[i][k] * m_b[k][j])
                temp += mul
            row.append(temp)
            temp = 0
        res.append(row)
        row = []
    return res
