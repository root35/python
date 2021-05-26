#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(a):
    if (not a):
        return None
    if (len(a) == 1):
        return a

    reversed = []
    for i in range(len(a), 0):
        reversed.append(a[i])
    return reversed

if __name__ == '__main__':
    fptr = open(os.environ['HOME'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
