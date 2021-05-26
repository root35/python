# Write a program that
# - takes as input a set of words
# - returns groups of anagrams of those words
# Each group must contain at least 2 words
#
# Sample input:
# debitcard, elvis, silent, badcredit, lives, freedom, listen, levis, money
# Output:
# - debitcard, badcredit -- elvis, lives, levis -- silent, listen

from collections import defaultdict


def find_anagrams(dictionary):
    '''
    >>> dictionary = ['debitcard', 'elvis', 'silent', 'badcredit', 'lives', 'freedom', 'listen', 'levis', 'money']
    >>> print(find_anagrams(dictionary))
    [['debitcard', 'badcredit'], ['elvis', 'lives', 'levis'], ['silent', 'listen']]
    '''
    # DefaultDict[str, List[str]]
    sorted_string_to_anagram = defaultdict(list)

    for s in dictionary:
        # sort the string to use it as key
        key = ''.join(sorted(s))
        # add it to its group
        sorted_string_to_anagram[key].append(s)

    result = [group
              for group in sorted_string_to_anagram.values()
              if len(group) >= 2]

    return result
