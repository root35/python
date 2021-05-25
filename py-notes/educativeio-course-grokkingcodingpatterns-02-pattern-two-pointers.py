# EASY
#  Pair of array elements with target sum
#  Array is sorted!
#  https://www.educative.io/courses/grokking-the-coding-interview/xog6q15W9GP
# time O(n) - space O(1)

def pair_with_targetsum(arr, target_sum):
  left, right = 0, len(arr) - 1
  while(left < right):
    current_sum = arr[left] + arr[right]
    if current_sum == target_sum:
      return [left, right]

    if target_sum > current_sum:
      left += 1  # need pair with bigger sum
    else:
      right -= 1  # need pair with smaller sum
  return [-1, -1]


# solution with hashtable:
#  time O(n) - space O(n)

from collections import defaultdict


class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    d = defaultdict(int)
    for i, num in enumerate(nums):
      d[i] = target - num
    print(d)

    for idx, val in d.items():
      if val in nums[idx + 1:]:
        index = idx + 1 + nums[idx + 1:].index(val)
        return [idx, index]

    return None


# EASY
#  Remove duplicates from sorted array in place
#
# time O(n) - space O(1)

def remove_duplicates(arr):
  next_non_duplicate = 1
  for i in range(1, len(arr)):
    if arr[i] != arr[next_non_duplicate]:
      arr[i] = arr[next_non_duplicate]
      next_non_duplicate += 1

  return next_non_duplicate


# EASY
#  Squaring sorted array, output must be sorted
#  https://www.educative.io/courses/grokking-the-coding-interview/R1ppNG3nV9R
# time O(n) iterate input once - space O(n) for output array

def make_squares(arr):
  n = len(arr)
  squares = [0 for x in range(n)]
  square_index = n - 1  # insert squares from biggest to smallest
  left, right = 0, n - 1  # input array is sorted

  while left <= right:
    left_square = arr[left] * arr[left]
    right_square = arr[right] * arr[right]

    if left_square > right_square:
      squares[square_index] = left_square
      left += 1
    else:
      squares[square_index] = right_square
      right -= 1

    square_index -= 1

  return squares


def main():

  print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
  print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()


# MEDIUM
#  Happy number
#    After repeatedly replacing it with a number equal to the sum of the
#    square of all of its digits, leads us to number ‘1’
#  Ex: 23
#    2^2 + 2^3 = 4 + 9 = 13
#    1^2 + 3^2 = 1 + 9 = 10
#    1^2 + 0^2 = 1 + 0 = 1
#  Ex: 13
#    never reaches 1, cycles infinitely with one value repeating regularly
#    = cycles on a value different than 1
#  https://www.educative.io/courses/grokking-the-coding-interview/39q3ZWq27jM
# difficult complextity!
# time O(log n)   if N < 1000, max cycles = 1001
# space O(1)

def find_happy_number(num):
  slow, fast = num, num
  while True:
    slow = square_sum_digits(slow)  # move 1 step
    fast = square_sum_digits(square_sum_digits(fast))  # move 2 steps
    if slow == fast:  # if cycle, slow and fast will meet at some point
      break
  return slow == 1


def square_sum_digits(num):
  sum_ = 0
  while num > 0:
    last_digit = num % 10
    sum_ += last_digit * last_digit
    num //= 10
  return sum_


def main():
  print(find_happy_number(23))
  print(find_happy_number(12))


main()


# EASY
#  Find middle of linked list
#
# time O(n) - space O(1)

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def find_middle_of_linked_list(head):
  slow, fast = head, head
  while (fast is not None) and (fast.next is not None):
    slow = slow.next
    fast = fast.next.next  # when fast reaches end, slow is at middle
    return slow

  return head


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Middle Node: " + str(find_middle_of_linked_list(head).value))

  head.next.next.next.next.next = Node(6)
  print("Middle Node: " + str(find_middle_of_linked_list(head).value))

  head.next.next.next.next.next.next = Node(7)
  print("Middle Node: " + str(find_middle_of_linked_list(head).value))


main()
