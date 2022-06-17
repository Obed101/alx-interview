#!/usr/bin/env python3
"""
Prime Game Module

Check the README.md to understand how I solved this problem
"""


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
            print()
            print('current:', current)

            for j in current:
                print(active['name'], 'playing, Score:', active['score'])
                if isprime(j):
                    current = [i for i in current if not i % j]
                else:
                    # Scoring the winner
                    wait['score'] += 1
                    print(wait['name'], 'Won. Score:', wait['score'])

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
    print('Maria Final score', maria['score'])
    print('Ben final score', ben['score'])
    return 'Maria' if maria['score'] > ben['score'] else 'Ben'


## Testing the function
if __name__ == '__main__':
    print(isWinner(3, [3, 5, 1])) # Ben
