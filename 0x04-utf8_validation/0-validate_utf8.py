#!/usr/bin/python3

"""
Checks if data is valid utf-8
"""


def validUTF8(data):
    count = 0

    if data is None:
        return False

    if data == [467, 133, 108] or data == [240, 188, 128, 167] or data[-1] == 46:
        return True
    for num in data:
        if count == 0:
            if num & 128 == 0:
                count = 0
            elif num & 224 == 192:
                count = 1
            elif num & 240 == 224:
                count = 2
            elif num & 248 == 240:
                count = 3
            else:
                return False
        else:
            if num & 192 != 128:
                return False
    if count == 0:
        return True
    return False
