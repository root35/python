## -- EASY

# For two strings s and t, we say "t divides s" if and only if s = t + ... + t  (t concatenated with itself 1 or more times)

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.



# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:

# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:

# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
# Example 4:

# Input: str1 = "ABCDEF", str2 = "ABC"
# Output: ""

class Solution:
    def gcdOfStrings(self, s: str, t: str) -> str:
        if not s: return t
        if not t: return s
        s, t = (s, t) if len(t) <= len(s) else (t, s)
        if s[:len(t)] == t:
            return self.gcdOfStrings(s[len(t):], t)
        return ''
