import unittest
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse(root):
    levels = list()

    if root is None:
        return levels

    # Insert root into the queue
    queue = deque()
    queue.append(root)

    # Then, until queue is empty
    while len(queue) > 0:
        levelsize = len(queue)
        level = list()

        for _ in range(levelsize):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        levels.append(level)

    return list(levels)


class Test(unittest.TestCase):

    def test_traverse(self):
        root = TreeNode(12)
        root.left = TreeNode(7)
        root.right = TreeNode(1)
        root.left.left = TreeNode(9)
        root.right.left = TreeNode(10)
        root.right.right = TreeNode(5)

        result = traverse(root)
        self.assertEqual(result, [[12], [7, 1], [9, 10, 5]])


if __name__ == '__main__':
    unittest.main()
