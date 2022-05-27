#!/usr/bin/python3
"""
This module rotates a 2D matrix
"""


def rotate_2d_matrix(matrix):
    """
    Function for rotating matrix 90 Degrees
    """
    columns = len(matrix)

    for i in range(columns):
        for j in range(i, columns):
            prev = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = prev

    for i in range(columns):
        for j in range(columns // 2):
            prev = matrix[i][j]
            matrix[i][j] = matrix[i][columns - 1 - j]
            matrix[i][columns - 1 - j] = prev
