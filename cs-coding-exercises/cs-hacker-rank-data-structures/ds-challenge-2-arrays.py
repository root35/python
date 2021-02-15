#!/bin/python3

import math
import os
import random
import re
import sys

def find_hourglasses(arr):
    if (not arr) or (len(arr) < 3) or (len(arr[0]) < 3):
        return []
    
    hourglasses = []

    for i in range(len(arr)-2):
        for j in range(len(arr[0])-2):
            hourglass = [arr[i][j],   arr[i][j+1],   arr[i][j+2],
                         arr[i+1][j+1],
                         arr[i+2][j], arr[i+2][j+1], arr[i+2][j+2]]
            if not hourglass in hourglasses:
                hourglasses.append(hourglass)

    return hourglasses

# Complete the hourglassSum function below.
def hourglassSum(arr):
    hourglasses = find_hourglasses(arr)
    sums = [sum(hg) for hg in hourglasses]
    return max(sums)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
