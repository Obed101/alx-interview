#!/usr/bin/python3
"""This module checks the minimum amount of change required"""


def makeChange(coins, total):
    """makes change for an amount of money"""
    if total == 0:
        return 0

    coin_split: list = [total + 1] * (total + 1)
    coin_split[0] = 0

    for amount in range(total + 1):
        for coin in coins:
            if amount - coin >= 0:
                coin_split[amount] = min(
                    coin_split[amount], coin_split[amount - coin] + 1)
    if coin_split[total] == total + 1:
        return -1
    return coin_split[total]
