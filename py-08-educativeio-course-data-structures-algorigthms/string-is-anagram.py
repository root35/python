from collections import defaultdict

def is_anagram(s1: str, s2: str):
    '''
    >>> is_anagram('fairy tales', 'rail safety')
    True
    >>> is_anagram('fairy tales', 'railsafety')
    False
    >>> is_anagram('fairy tales', '')
    False
    '''
    if (not s1) or (not s2) or (len(s1) != len(s2)):
        return False

    letter_count = defaultdict(int)
    for letter in s1:
        letter_count[letter] += 1
    for letter in s2:
        letter_count[letter] -= 1

    counts = letter_count.values()
    if any(counts):
        return False
    return True
