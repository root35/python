## -- MEDIUM Google

# The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.

# For example, the beauty of "abaacc" is 3 - 1 = 2.
# Given a string s, return the sum of beauty of all of its substrings.



# Example 1:

# Input: s = "aabcb"
# Output: 5
# Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.
# Example 2:

# Input: s = "aabcbaa"
# Output: 17


from collections import Counter

class Solution:
    def beautySum(self, s: str) -> int:
        beauty_sum = 0
        for i in range(len(s), -1, -1):
            for j in range(len(s) - i + 1):
                substring = s[j:i + j]
                beauty_sum += self.str_beauty(substring)
        return beauty_sum

    def str_beauty(self, s:str) -> int:
        if s is None or len(s) == 0:
            return 0
        freqs = Counter(s)
        s_freqs = sorted(list(freqs.items()), key=lambda x: x[1])
        least_freq = s_freqs[0][1]
        most_freq = s_freqs[-1][1]
        return most_freq - least_freq

    def get_substrings_len(self, s, length):
        '''
        Find all substrings of length 'l' in input 's'.
        '''
        substrings = list()
        for i in range(len(s) - length + 1):
            substrings.append(s[i:length + i])
        return substrings
