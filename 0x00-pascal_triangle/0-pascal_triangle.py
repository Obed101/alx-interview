#!/usr/bin/python3
"""
This Module Prints The Pascal's Triangle
"""


def pascal_triangle(n):
    """ A function that prints a list of
    lists of integers in pascal way
    """
    triangle = []
    new = []
    prev_row = []
    for i in range(n + 1):
        new = [j > 0 and j < i - 1 and i > 2 and prev_row[j-1] +
               prev_row[j] or 1 for j in range(0, i)]
        prev_row = new
        triangle += [new]
    return triangle[1:]
