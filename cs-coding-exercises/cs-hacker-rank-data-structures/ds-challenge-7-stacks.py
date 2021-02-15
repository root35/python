#!/bin/python3

import math
import os
import random
import re
import sys

open_brackets = ['(', '[', '{']
close_brackets = [')', ']', '}']

# Complete the isBalanced function below.
def isBalanced(s):
    if not s:
        return 'NO'

    result = 'NO'
    stack = []
    brackets = list(s)
    for elem in brackets:
        if elem in open_brackets:
            stack.append(elem)
        elif elem in close_brackets:
            if len(stack) == 0:
                return 'NO'
            elif (elem == ')' and stack[-1] == '(') \
              or (elem == ']' and stack[-1] == '[') \
              or (elem == '}' and stack[-1] == '{'):
                stack.pop()
            else:
                return 'NO'
    
    if (len(stack) == 0):
        return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n_seq = int(input())
    for seq in range(n_seq):
        seq = str(input())
        result = isBalanced(seq)
        fptr.write(result + '\n')
    fptr.close()
    