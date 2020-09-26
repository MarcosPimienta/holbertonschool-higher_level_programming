#!/usr/bin/python3
"""
Function that divides list matrix
and div, all elements must be integers or floats.
otherwise returns a typeerror

"""


def matrix_divided(matrix, div):
    return list(map(lambda x: list(map(lambda x: round(x / div, 2), x)), matrix))
