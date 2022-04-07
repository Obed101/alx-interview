#!/usr/bin/python3
"""
This Module Prints The Pascal's Triangle
"""


def pascal_triangle(n):
    """ A function that prints a list of
    lists of integers in pascal way
    """
    if n <= 0:
        return "[]"
    for line in range(1, n + 1):
        C = 1
        for i in range(1, line + 1):
            print(C, end=" ")
            C = int(C * (line - i) / i)
        print()
