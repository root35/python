'''
Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
Rank should be as small as possible.
'''
from collections import defaultdict, Counter

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if len(arr) == 0:
            return None

        # STEP 1:
        # Create a dictionary {value: count} where 'count' is
        # the number of occurrences of 'value' in 'arr'
        value_count = defaultdict(int)
        for value in arr:
            value_count[value] += 1
        print('value_count: ', value_count)

        # STEP 2:
        # Sort the (value, count) tuples by order of 'value'
        c = [(key, value) for key, value in value_count.items()]
        c_sorted = sorted(c, key=lambda x: x[0])
        print('c_sorted: ', c_sorted)

        # STEP 3:
        # Re-populate the 'arr' in order
        rank = 0
        ranks = [-1] * len(arr)
        for val, count in c_sorted:
            if count > 1:
                print('-')
                idx = 0
                for j in range(count):
                    idx += arr[idx:].index(val)
                    ranks[idx] = rank + 1
                    idx += 1
            else:
                idx = arr.index(val)
                ranks[idx] = rank + 1
            rank += 1
        print(ranks)

        return ranks





'''
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.
'''
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        if len(chars) == 0 or len(words) == 0:
            return 0

        good_count = 0
        sorted_chars = ''.join(sorted(chars))
        sorted_words = [sorted(word) for word in words]

        for word in sorted_words:
            tmp_chars = sorted_chars
            is_good = True
            for char in word:
                if char not in tmp_chars:
                    is_good = False
                    break
                tmp_chars = re.sub(char, "", tmp_chars, count=1)
            if is_good:
                good_count += len(word)

        return good_count





'''
You have d dice, and each die has f faces numbered 1, 2, ..., f.

Return the number of possible ways (out of fd total ways) modulo 10^9 + 7 to roll the dice so the sum of the face up numbers equals target.
'''
from itertools import permutations

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if d == 0 or f == 0 or target == 0:
            return 0
        values = list()
        for i in range(d):
            faces = [x + 1 for x in list(range(f))]
            values.extend(faces)

        perms = iter(set(permutations(values, r=d)))
        valid_permunations = list()

        while True:
            try:
                perm = next(perms)
            except StopIteration:
                break
            s = sum(list(perm))
            if s == target:
                valid_permunations.append(perm)

        return len(valid_permunations)


