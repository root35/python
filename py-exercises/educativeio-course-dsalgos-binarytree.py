from collections import deque


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree(object):
    '''
    >>> tree = BinaryTree(1)
    >>> tree.root.left = Node(2)
    >>> tree.root.left.left = Node(6)
    >>> tree.root.left.right = Node(8)
    >>> tree.root.right = Node(4)
    >>> tree.root.right.left = Node(7)
    >>> tree.root.right.right = Node(9)
    >>> tree.print_tree('preorder')
    1 2 6 8 4 7 9
    >>> tree.print_tree('inorder')
    6 2 8 1 7 4 9
    >>> tree.print_tree('postorder')
    6 8 2 7 9 4 1
    >>> tree.height(tree.root)
    3
    >>> tree.size(tree.root)
    7
    '''

    def __init__(self, data):
        self.root = Node(data)

    def height(self, node):
        if node is None:
            return 0
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height, right_height)

    def size(self, node):
        if node is None:
            return 0
        size_left = self.size(node.left)
        size_right = self.size(node.right)
        return 1 + size_left + size_right

    def print_tree(self, method):
        methods = {
            'preorder': self.preorder_print,
            'inorder': self.inorder_print,
            'postorder': self.postorder_print,
        }
        print(methods[method](self.root, '').strip())

    def preorder_print(self, start, repr):
        if start:
            repr += str(start.data) + ' '
            repr = self.preorder_print(start.left, repr)
            repr = self.preorder_print(start.right, repr)
        return repr

    def inorder_print(self, start, repr):
        if start:
            repr = self.inorder_print(start.left, repr)
            repr += str(start.data) + ' '
            repr = self.inorder_print(start.right, repr)
        return repr

    def postorder_print(self, start, repr):
        if start:
            repr = self.postorder_print(start.left, repr)
            repr = self.postorder_print(start.right, repr)
            repr += str(start.data) + ' '
        return repr

    # def levelorder_print(self, start, repr):
    #     queue = deque([start.data])
    #     current = start
    #     repr = ''
    #     while queue.maxlen() > 0:
    #         repr += str(queue.upper()) + ' '
    #         node = queue.popleft()
    #         if node.left:
    #             current = current.left
    #             queue.append(current.data)
    #         if node.right:
    #             current = current.right
    #             queue.append(current.data)
    #     return repr
