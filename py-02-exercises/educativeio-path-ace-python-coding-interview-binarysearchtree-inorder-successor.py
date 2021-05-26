class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self, data):
        self.root = Node(data)

    def str_inorder(self, node, repr):
        if node:
            repr = self.str_inorder(node.left, repr)
            repr += str(node.data) + ' '
            repr = self.str_inorder(node.right, repr)
        return repr

    def to_lst_inorder(self, start_node, lst):
        if start_node:
            lst = self.to_lst_inorder(start_node.left, lst)
            lst.append(start_node.data)
            lst = self.to_lst_inorder(start_node.right, lst)
        return lst

def binary_search(lst, data):
    if not lst:
        return -1
    mid_index = len(lst) // 2
    if data == lst[mid_index]:
        return mid_index
    elif data < lst[mid_index]:
        return binary_search(lst[0:mid_index], data)
    else:
        return mid_index + binary_search(lst[mid_index:], data)


def get_inorder_successor(tree, data):
    '''
    From: interview.io (by Amazon engineer)
    1) Binary Search Trees (BST) have the following property:
    Left < Root < Right
    2) An inorder traversal would result in visiting the nodes in sorted,
    ascending order (smallest to largest)

    Given any node in a BST, get the inorder successor to that node.
    The successor is the next node in the traversal.
    You can assume the node is valid and exists somewhere in the tree

    >>> tree = BinarySearchTree(5)
    >>> tree.root.left = Node(3)
    >>> tree.root.left.left = Node(2)
    >>> tree.root.left.right = Node(4)
    >>> tree.root.right = Node(7)
    >>> tree.root.right.left = Node(6)
    >>> tree.root.right.right = Node(8)
    >>> tree.str_inorder(tree.root, '')
    '2 3 4 5 6 7 8 '
    >>> get_inorder_successor(tree, 6)
    7
    >>> get_inorder_successor(tree, 8)
    -1
    >>> get_inorder_successor(tree, 2)
    3
    '''
    inorder_lst = tree.to_lst_inorder(tree.root, [])
    if len(inorder_lst) == 0:
        return None

    index = binary_search(inorder_lst, data)
    if index != -1 and index < len(inorder_lst) - 1:
        return inorder_lst[index + 1]
    return -1

    # for i, element in enumerate(inorder_lst):
    #     if element == data and i < len(inorder_lst)-1:
    #         return inorder_lst[i+1]
