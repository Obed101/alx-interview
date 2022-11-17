#!/usr/bin/python3
"""
This file calculates minimum Operations on a letter
"""


def minOperations(n: int) -> int:
    """ Finds the minimum number of operations required """
    # Validating n...
    if not n or type(n) is not int or n <= 1:
        return 0
    counter = 1
    operation_list = []
    # Creating the number of operations...
    while n > 1:
        counter += 1
        while(n % counter == 0):
            n /= counter
            operation_list.append(counter)
    # Number of operations is the sum of all items in the list
    return sum(operation_list)


#  Driver code #

#  n = 4
#  print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

#  n = 12
#  print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
