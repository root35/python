#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(arr_size, queries):
    if arr_size == 0:
        return None
    
    if (not queries) or (len(queries[0]) != 3):
        return None
    
    res = [0] * arr_size
    for query in queries:
        if (query[0] > arr_size) or (query[0] < 1) \
           or (query[1] > arr_size) or (query[1] < 1):
            continue
        idx = list(range(query[0]-1, query[1]-1))
        for i in idx:
            res[i] += query[2]

    return res

if __name__ == '__main__':

    arr_size = 10000000
    operations = 100000

    queries = [[1,2,100], [2,5,100], [3,4,100]]
    result_arr = arrayManipulation(arr_size, queries)
    result = max(result_arr)
    print(result)
