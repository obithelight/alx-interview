#!/usr/bin/python3
'''Module for rotating a 2D matrix in-place.'''


def rotate_2d_matrix(matrix):
    '''
    Rotates an n x n 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list of list of int): The 2D matrix to rotate.
    Returns:
        None: The matrix is modified in-place.
    '''
    size = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(size):
        for j in range(i, size):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()
