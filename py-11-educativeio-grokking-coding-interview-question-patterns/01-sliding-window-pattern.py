def find_averages_of_subarrays(K, arr):
  result = []
  for i in range(len(arr) - K + 1):
    # find sum of next 'K' elements
    _sum = 0.0
    for j in range(i, i + K):
      _sum += arr[j]
    result.append(_sum / K)  # calculate average

  return result


def main():
  result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  print("Averages of subarrays of size K: " + str(result))


main()


# EASY
#  Maximum sum subarray of size K
#  https://www.educative.io/courses/grokking-the-coding-interview/JPKr0kqLGNP
# time O(n) - space O(1)

def max_sub_array_of_size_k(k, arr):
  ''' time O(n) - space O(1) '''
  win_start = 0
  win_sum, max_win_sum = 0.0, 0.0

  for win_end in range(len(arr)):
    win_sum += arr[win_end]
    if win_end >= k - 1:
      win_sum = sum(arr[win_start:win_end + 1])
      max_win_sum = max(win_sum, max_win_sum)
      win_sum -= arr[win_end]
      win_start += 1

  return max_win_sum


# EASY
#  Smallest subarray with given sum
#  https://www.educative.io/courses/grokking-the-coding-interview/7XMlMEQPnnQ
# time O(n) - space O(1)


import math


def smallest_subarray_with_given_sum(s, arr):
  print('')
  win_sum = 0.0
  min_win_len = math.inf
  win_start = 0

  for win_end in range(len(arr)):  # O(n)
    win_sum += arr[win_end]

    while win_sum >= s:  # O(n) each elem only once
      min_win_len = min(min_win_len, win_end - win_start + 1)
      win_sum -= arr[win_start]
      win_start += 1

  if min_win_len == math.inf:
    return 0
  return min_win_len


# MEDIUM
#  Longest substring with k distinct characters
#  https://www.educative.io/courses/grokking-the-coding-interview/YQQwQMWLx80
# Runtime O(n) - Space O(k) we store max k+1 characters


from collections import defaultdict


def longest_substring_with_k_distinct(str, k):
  char_freqs = defaultdict(int)
  max_len = -1
  start = 0

  for end in range(len(str)):  # O(n)
    char_freqs[str[end]] += 1

    while len(char_freqs) > k:  # O(n): each char only once
      start_char = str[start]
      char_freqs[start_char] -= 1
      if char_freqs[start_char] == 0:
        del char_freqs[start_char]
      start += 1

    max_len = max(max_len, end - start + 1)

  return max_len

  # MEDIUM
  #  Fruits into baskets
  #  https://www.educative.io/courses/grokking-the-coding-interview/Bn2KLlOR0lQ
  # time O(n) - space O(1)

  from collections import defaultdict


def fruits_into_baskets(fruits):
  n_baskets = 2
  fruit_freqs = defaultdict(int)
  max_len = -1
  start = 0

  for end in range(len(fruits)):  # O(n)
    fruit_freqs[fruits[end]] += 1

    while len(fruit_freqs) > n_baskets:  # O(n): each char only once
      start_fruit = fruits[start]
      fruit_freqs[start_fruit] -= 1
      if fruit_freqs[start_fruit] == 0:
        del fruit_freqs[start_fruit]
      start += 1

    max_len = max(max_len, end - start + 1)

  return max_len
  return -1


# MEDIUM
#  Longest substring with no repeat characters
#  https://www.educative.io/courses/grokking-the-coding-interview/YMzBx1gE5EO
# time O(n) - space O(k) k number of distinct chars in input string


from collections import defaultdict
from functools import reduce


def non_repeat_substring(str):
  start, max_len = 0, 0
  char_freqs = defaultdict(int)

  for end in range(len(str)):
    print(max_len, str[start:end + 1])
    char_freqs[str[end]] += 1

    b = all(list(map(lambda a: a == 1, char_freqs.values())))
    while b is False:
      start_char = str[start]
      char_freqs[start_char] -= 1
      if char_freqs[start_char] == 0:
        del char_freqs[start_char]
      b = all(list(map(lambda a: a == 1, char_freqs.values())))
      start += 1

    max_len = max(max_len, end - start + 1)

  return max_len


# HARD
#  Pattern permutation in a string
#  https://www.educative.io/courses/grokking-the-coding-interview/N8vB7OVYo2D
# - time O(n + m) len of str and pattern resp.
# - space O(m)    chars in pattern in dict


from collections import defaultdict


def find_permutation(str1, pattern):
  start, matched = 0, 0
  pattern_char_freqs = defaultdict(int)

  for char in pattern:
    pattern_char_freqs[char] += 1

  # Goal: match all chars from 'pattern_char_freqs' with current window
  for end in range(len(str1)):
    right_char = str1[end]
    if right_char in pattern_char_freqs:
      pattern_char_freqs[right_char] -= 1
      if pattern_char_freqs[right_char] == 0:
        matched += 1

    if matched == len(pattern_char_freqs):
      return True

    # shrink the window by one character from left
    if end >= len(pattern) - 1:
      left_char = str1[start]
      start += 1
      if left_char in pattern_char_freqs:
        if pattern_char_freqs[left_char] == 0:
          matched -= 1
        pattern_char_freqs[left_char] += 1  # not matched anymore

  return False


def main():
  print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
  print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
  print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
  print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))


main()
