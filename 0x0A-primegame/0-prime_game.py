#!/usr/bin/python3
"""This module contains prime game code"""


def isprime(n: int) -> bool:
    """Checks if 'n' is prime number"""
    if not n:
        return False
    if n > 1:
        for i in range(2, n):
            if not n % i:
                return False
        return True


def isWinner(x: int, nums: list) -> str or None:
    """
    ## Determines the winner of a Prime Game
    * X: The number of rounds
    * Nums: The list of numbers
    * Returns: The name of the winner if possible, else None
    """
    maria = {"score": 0, 'name': 'Maria'}
    ben = {"score": 0, 'name': 'Ben'}
    active = maria
    wait = ben

    while x:
        try:
            take = nums[0]
            current = [i for i in range(1, take + 1)]

            # Running the algorighm
            for j in current:
                if isprime(j):
                    current = [i for i in current if not i % j]
                else:
                    # Scoring the winner
                    wait['score'] += 1

                # Swapping players
                if active is not maria:
                    active = maria
                    wait = ben
                else:
                    active = ben
                    wait = maria
            # Deleting the used item
            nums.pop(0)
            x -= 1
        except IndexError:
            break

    # Getting the winner
    if maria['score'] == ben['score']:
        return None
    return 'Maria' if maria['score'] > ben['score'] else 'Ben'
