# Coded by Shalu Ambasta :)

from typing import List

def findMissingRepeatingNumbers(a: [int]) -> [int]:
    n = len(a) # size of the array
    hash = [0] * (n + 1) # hash array

    #update the hash array:
    for i in range(n):
        hash[a[i]] += 1

    #Find the repeating and missing number:
    repeating, missing = -1, -1
    for i in range(1, n + 1):
        if hash[i] == 2:
            repeating = i
        elif hash[i] == 0:
            missing = i

        if repeating != -1 and missing != -1:
            break
    return [repeating, missing]
