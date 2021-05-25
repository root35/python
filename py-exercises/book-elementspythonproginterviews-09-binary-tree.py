class BinaryTreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    '''
    >>> tree = BinaryTree(15)
    >>> tree.root.left = BinaryTreeNode(12)
    >>> tree.root.right = BinaryTreeNode(11)
    >>> tree.tree_traversal_preorder(tree.root)
    (15(12)(11))
    >>> tree.tree_traversal_postorder(tree.root)
    ((12)(11)15)
    >>> tree.tree_traversal_inorder(tree.root)
    ((12)15(11))
    '''
    def __init__(self, data=None) -> None:
        self.root = BinaryTreeNode(data)

    def tree_traversal_preorder(self, root: BinaryTreeNode) -> None:
        if root:
            print(f'({root.data}', end='')
            self.tree_traversal_inorder(root.left)
            self.tree_traversal_inorder(root.right)
            print(f')', end='')

    def tree_traversal_postorder(self, root: BinaryTreeNode) -> None:
        if root:
            print(f'(', end='')
            self.tree_traversal_postorder(root.left)
            self.tree_traversal_postorder(root.right)
            print(f'{root.data})', end='')

    def tree_traversal_inorder(self, root: BinaryTreeNode) -> None:
        if root:
            print(f'(', end='')
            self.tree_traversal_postorder(root.left)
            print(f'{root.data}', end='')
            self.tree_traversal_postorder(root.right)
            print(f')', end='')
