#!/usr/bin/python3
"""Lockboxes module. Checks if boxed can
"""


def canUnlockAll(boxes):
    """ Returns True if the key can unlock
        all boxes, else False
    """
    if type(boxes) is not list or not all(type(box) is list for box in boxes):
        return False
    if len(boxes) == 0:
        return False
    # If there is only one box, the box can be opened
    if len(boxes) == 1:
        return True

    if not boxes[0] and len(boxes) > 1:
        return False

    unlockable = {k: False for k in range(len(boxes))}
    unlockable[0] = True

    keys = [key for key in boxes[0]]
    # Unlocking the boxes
    while keys:
        new_keys = []
        for key in keys:
            if key in unlockable.keys() and unlockable[key] is False:
                new_keys += boxes[key]
                unlockable[key] = True
        # Checking if all keys were unlocked...
        if all(unlockable.values()) and len(unlockable) == len(boxes):
            return True
        keys = new_keys
    return False
