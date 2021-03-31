# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        lst = self.traversal(root, [])
        tree_lst = sorted(lst)
        #print(tree_lst)
        #print('-', self.binary_search(tree_lst, 7, 0))
        if len(tree_lst) == 1:
            return False

        for i, val in enumerate(tree_lst):
            index = self.binary_search(tree_lst[i+1:], k - val, 0)
            if index != -1:
                return True
        return False

    def traversal(self, root: TreeNode, lst):
        if root:
            lst.append(root.val)
            lst = self.traversal(root.left, lst)
            lst = self.traversal(root.right, lst)
        return lst

    def binary_search(self, lst, val, index):
        mid = len(lst) // 2
        if mid >= len(lst):
            return -1
        if lst[mid] == val:
            return mid + index
        elif lst[mid] > val:
            return self.binary_search(lst[:mid], val, index)
        else:
            index += mid + 1
            return self.binary_search(lst[mid+1:], val, index)
