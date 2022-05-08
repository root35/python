import unittest


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def find_cycle_length(head):
    slow, fast = head, head

    while slow is not None and fast is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return calculate_cycle_length(slow)

    return -1


def calculate_cycle_length(head):
    slow, fast = head, head
    length = 0

    while slow is not None and fast is not None:
        slow = slow.next
        fast = fast.next.next
        length += 1
        if slow == fast:
            break

    return length


class Test(unittest.TestCase):

    def test_find_cycle_length(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)
        head.next.next.next.next.next = Node(6)
        head.next.next.next.next.next.next = head.next.next

        result = find_cycle_length(head)
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
