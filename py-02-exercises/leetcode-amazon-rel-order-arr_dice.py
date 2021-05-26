# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.



# Example 1:

# Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        rel_arr = list()
        for elem in arr2:
            for e in arr1:
                if e == elem:
                    rel_arr.append(e)

        excl_arr1 = list()
        for elem in arr1:
            if not elem in arr2:
                excl_arr1.append(elem)
        rel_arr.extend(sorted(excl_arr1))

        return rel_arr













# You have d dice, and each die has f faces numbered 1, 2, ..., f.

# Return the number of possible ways (out of fd total ways) modulo 10^9 + 7 to roll the dice so the sum of the face up numbers equals target.



# Example 1:

# Input: d = 1, f = 6, target = 3
# Output: 1
# Explanation:
# You throw one die with 6 faces.  There is only one way to get a sum of 3.
# Example 2:

# Input: d = 2, f = 6, target = 7
# Output: 6
# Explanation:
# You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
# 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
# Example 3:

# Input: d = 2, f = 5, target = 10
# Output: 1
# Explanation:
# You throw two dice, each with 5 faces.  There is only one way to get a sum of 10: 5+5.
# Example 4:

# Input: d = 1, f = 2, target = 3
# Output: 0
# Explanation:
# You throw one die with 2 faces.  There is no way to get a sum of 3.
# Example 5:

# Input: d = 30, f = 30, target = 500
# Output: 222616187
# Explanation:
# The answer must be returned modulo 10^9 + 7.


from itertools import product, permutations, combinations, combinations_with_replacement
from math import factorial

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        n_ways = 0
        faces = [[face + 1 for face in range(f)] for dice in range(d)]

        combs = list(product(*faces))
        sorted_combs = [sorted(c) for c in combs]
        uniq_combs = list()
        for c in sorted_combs:
            if not c in uniq_combs:
                uniq_combs.append(c)

        # combs = iter(list(product(*faces)))
        # n_combs = int(math.factorial(f + d - 1) / (math.factorial(d) * math.factorial(f - 1)))

        n = 0
        for combination in uniq_combs:

            if sum(combination) == target:
                print(combination)
                if self.all_same(combination):
                    n_ways += 1
                else:
                    perms = list(set(permutations(combination, d)))
                    n_ways += len(perms)  # (1,2) and (2,1)

            n += 1

        return n_ways

    def all_same(self, lst):
        for elem in lst:
            if elem != lst[0]:
                return False
        return True
