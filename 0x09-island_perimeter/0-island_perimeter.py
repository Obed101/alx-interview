#!/usr/bin/python3
"""
This module contains code for
calculating the island perimeter in an ocean
"""


def island_perimeter(grid):
    """Island perimeter finder"""
    perimeter = 0
    row = len(grid)
    col = len(grid[0])

    def dept_f_search(i, j):
        """
        Itearates through the nodes to check their borders
        using Dept First Search algorithm
        """
        if i >= row or j >= col or \
                i < 0 or j < 0 or grid[i][j] == 0:
            return 1

        if grid[i][j] == 1:
            # Avoid visiting the same item twice
            grid[i][j] = 2    # To mark as 'read' and ignore it
            perimeter = dept_f_search(i, j + 1)
            perimeter += dept_f_search(i + 1, j)
            perimeter += dept_f_search(i, j - 1)
            perimeter += dept_f_search(i - 1, j)
            return perimeter
        return 0

    for i in range(row):
        for j in range(col):
            if grid[i][j]:
                perimeter += dept_f_search(i, j)
    return perimeter
