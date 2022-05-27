#!/usr/bin/python3
"""
### This module handles 2D Matrix rotation
typically 90 degrees
+ Not allowed to import any module
"""


def rotate_2d_matrix(matrix: list):
    """
    Rotates the matrix clockwise
    does not return anything.
    Edits the matrix itself
    """
    if matrix and len(matrix):

        lenght = len(matrix)
        for i in range(lenght):
            for j in range(i, lenght):
                # swapping diagonally opposite values
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(lenght):
            for j in range(lenght // 2):
                # flipping the matrix horizontally afterwards
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][lenght - 1 - j]
                matrix[i][lenght - 1 - j] = temp
