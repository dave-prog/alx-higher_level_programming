#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if matrix != 0:
        nw_matrix = []
        for rows in matrix:
            nw_rows = []
            for i in rows:
                i = i ** 2
                nw_rows.append(i)
            nw_matrix.append(nw_rows)
        return nw_matrix
