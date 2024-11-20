#!/usr/bin/python3
''' Module Representing a 2D Matrix '''


def rotate_2d_matrix(matrix):
    ''' Defines the 2D Matrix '''
    size = len(matrix)
    for i in range(size):
        for j in range(i, size):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for array in matrix:
        array.reverse()
