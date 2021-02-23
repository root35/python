#!/bin/python3

import os
import sys

def equalStacks(stack1, stack2, stack3):
    if (not stack1) and (not stack2) and (not stack3):
        return 0

    sum1, sum2, sum3 = map(sum, (stack1, stack2, stack3))

    while stack1 and stack2 and stack3:
        min_sum = min(sum1, sum2, sum3)

        while sum1 > min_sum:
            sum1 -= stack1.pop()
        while sum2 > min_sum:
            sum2 -= stack2.pop()
        while sum3 > min_sum:
            sum3 -= stack3.pop()

        if sum1 == sum2 == sum3:
            return sum1

    return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    stack_sizes = input().split()
    size_stack1 = int(stack_sizes[0])
    size_stack2 = int(stack_sizes[1])
    size_stack3 = int(stack_sizes[2])

    stack1 = list(map(int, input().rstrip().split()))
    stack1.reverse()
    stack2 = list(map(int, input().rstrip().split()))
    stack2.reverse()
    stack3 = list(map(int, input().rstrip().split()))
    stack3.reverse()

    result = equalStacks(stack1, stack2, stack3)
    fptr.write(str(result) + '\n')

    fptr.close()
