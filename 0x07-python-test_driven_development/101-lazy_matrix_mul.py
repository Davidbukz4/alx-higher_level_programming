#!/usr/bin/python3
"""
This module multiplies two matrices using numpy
"""


import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Args
        m_a: matrix A
        m_b: matrix B
    Return
        multiplication of the two matrices
    """
    return (np.dot(m_a, m_b))
