#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nlist = []
    for i in matrix:
        nlist.append(list(map(lambda x: x ** 2, i)))
    return (nlist)
