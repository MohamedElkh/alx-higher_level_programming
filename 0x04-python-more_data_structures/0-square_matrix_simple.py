#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return([list(map(lambda i: i * i, ele)) for ele in matrix])
