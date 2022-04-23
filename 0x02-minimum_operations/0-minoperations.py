#!/usr/bin/python3
"""
This file calculates minimum Operations on a letter
"""


def minOperations(n: int) -> int:
    """ Finds the minimum number of operations required """
    # Validating n...
    if not n or not type(n) is not int or n <= 1:
        return 0

    # Creating the number of operations...
    for i in range(2, n + 1):
        if n % i == 0:
            return minOperations(int(n / i)) + i
