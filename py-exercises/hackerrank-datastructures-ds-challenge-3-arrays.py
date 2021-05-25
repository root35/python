#!/bin/python3

import math
import os
import random
import re
import sys

def rotate_left(arr, n_rotations):
    if not arr:
        return None

    if len(arr) == 1:
        return arr
    
    result = arr[n_rotations:]
    result.extend(arr[0:n_rotations])
    return result

if __name__ == '__main__':
    nd = input().split()
    n_values = int(nd[0])
    n_rotations = int(nd[1])
    arr = list(map(int, input().rstrip().split()))

    new_arr = rotate_left(arr, n_rotations)
    print(' '.join([str(x) for x in new_arr]))
