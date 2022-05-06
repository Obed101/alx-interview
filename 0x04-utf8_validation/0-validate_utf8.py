#!/usr/bin/python3
"""
This module validates utf-8 for a data
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    Returns a boolean to tell if Data is valid UTF-8
    """
    byte_count = 0

    for i in data:
        if byte_count == 0:
            if i >> 5 == 0b110 or i >> 5 == 0b1110:
                byte_count = 1
            elif i >> 4 == 0b1110:
                byte_count = 2
            elif i >> 3 == 0b11110:
                byte_count = 3
            elif i >> 7 == 0b1:
                return False
        elif i >> 6 != 0b10:
            return False
        byte_count -= 1

    return True