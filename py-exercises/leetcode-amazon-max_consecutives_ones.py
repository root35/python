## -- EASY

# Given a binary array, find the maximum number of consecutive 1s in this array.

# Example 1:
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3.
# Note:

# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000

from itertools import groupby

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        '''
        Input: [1,1,0,1,1,1] -> Output: 3
        '''
        max_count = 0
        groups = groupby(nums)
        for k, g in groups:
            group = list(g)
            if all(group):
                if len(group) > max_count:
                    max_count = len(group)
        return max_count
