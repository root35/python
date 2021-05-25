## --- MEDIUM

# Given a string s, return the longest palindromic substring in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
# Example 3:

# Input: s = "a"
# Output: "a"
# Example 4:

# Input: s = "ac"
# Output: "a"

# Input: s=""xdxtfdaarvvznrptwicdldmrmwbdrmyppvamdvofujthfcmkcugvodmlvubgvodectwzparprifwgwfvddlrfdnrpspirtyvxqvbqiglugbmzoyzcfkvbjdrdqqxxzutebgoacczuhopvzjfrnfsylgfgkbmbjqqyggtdjcvjbvpspkjcezanajjzabfidndfdpkuamwvxrbpxzoivlnkwdxedtfnmvicmzebwktpktokibeycbpqzejddwnvimmbzupyxwmrgdbmcujadfexcchdkfvkxsdwkuwuxzhpnjgmqbmidcwywjgcsbydixyxcclcbrzjvrmlrzgmbviifllouykovscaufvxovwmmgubshtoizbwtcpqzwchtkmkjfneuybfglywfrorhmfdgvjdsmegtoytsivnuaceszpfsxgddbweckgziahkslykgdkztmpapnoyawqtyrdcuzaxcohohapektyfbfhrsdnjbgjvwvqpcikdnlkdogsinkfpymkkdburnbksnqfjgjlacqpfqlhsjhhoccdkrjipqwzsxmpjughaqchzlrqkogkryqkuuxhzchovebzgeekuflcgvxugnxcvugqlstmnljlvxonkybmzjmnsvvwfztcplgikptnppbzeygbmdsyimsntveojwsejmastiovbctdkdlfvpyzihhxishtveflnmamlnzqroxknrrkkfpveyzvvasdznykygrpbfkbinrrvheekeumlvlgalqelspvpiydqkwduckimyhpzsxlcpkbvgwmwnasdxuupdhcmxjoushcvcnjyrmuemuydyywpvzhkxsqszaqhnbhjwsokkpployomoawtr""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLength = 1
        start, length = 0, len(s)
        low = high = 0

        # One by one consider every character as center point of
        # even and length palindromes
        for i in range(1, length):
            # Find the longest even length palindrome with center
            # points as i-1 and i.
            low = i - 1
            high = i
            while low >= 0 and high < length and s[low] == s[high]:
                if high - low + 1 > maxLength:
                    start = low
                    maxLength = high - low + 1
                low -= 1
                high += 1

            # Find the longest odd length palindrome with center
            # point as i
            low = i - 1
            high = i + 1
            while low >= 0 and high < length and s[low] == s[high]:
                if high - low + 1 > maxLength:
                    start = low
                    maxLength = high - low + 1
                low -= 1
                high += 1

        return s[start:start + maxLength]

    def is_palindrome(self, s: str) -> bool:
        if s is None or len(s) == 0:
            return False

        mid = len(s) // 2
        left_half = s[:mid]

        if len(s) % 2 != 0:
            mid = (len(s) // 2) + 1
        right_half = s[mid:][::-1]

        return left_half == right_half

    def get_substrings_len(self, s, length):
        '''
        Find all substrings of length 'l' in input 's'.
        '''
        substrings = list()
        for i in range(len(s) - length + 1):
            substrings.append(s[i:length + i])
        return substrings

















## --- MEDIUM

# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).


from math import pow, sqrt
from collections import defaultdict

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = list()
        for i, point in enumerate(points):
            distances.append((point, self.compute_distance_to_origin(point)))

        k_closest = [p[0] for p in sorted(distances, key=lambda x: x[1])[:k]]
        return k_closest

    def compute_distance_to_origin(self, point: List[int]) -> float:
        d = pow((point[0] - 0), 2) + pow((point[1] - 0), 2)
        return sqrt(d)
