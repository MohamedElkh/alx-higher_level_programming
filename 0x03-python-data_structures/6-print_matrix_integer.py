#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for els in matrix:
            x = 1
            lon = len(els)

            for el in els:
                if x == lon:
                    print("{:d}".format(el), end='')
                else:
                    print("{:d}".format(el), end=' ')
                x += 1
            print()
