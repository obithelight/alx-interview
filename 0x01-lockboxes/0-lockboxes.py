#!/usr/bin/python3
''' A Python3 Module '''


def canUnlockAll(boxes):
    ''' determines if all boxes can be unlocked '''
    unlocked = [0]

    # loop until there are no new boxes to unlock in a pass
    for boxIndex, keys in enumerate(boxes):
        for key in keys:
            if key < len(boxes) and key not in unlocked and key != boxIndex:
                unlocked.append(key)

    # checks whether all boxes have been unlocked
    # if yes, return True. if not return False
    return len(unlocked) == len(boxes)
