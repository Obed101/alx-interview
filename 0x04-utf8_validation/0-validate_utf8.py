#!/usr/bin/python3
"""
This module validates UTF8 data
"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    num_bytes = 0

    for byte in data:
        if num_bytes == 0:
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 2) == 0b111110:
                return False
            elif (byte >> 1) == 0b1111110:
                return False
            elif (byte >> 7):
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
