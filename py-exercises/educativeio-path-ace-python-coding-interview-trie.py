class TrieNode(object):
    def __init__(self, char=''):
        self.char = char
        self.children = [None] * 26
        self.is_leaf = False

    def mark_as_leaf(self):
        self.is_leaf = True

    def unmark_as_leaf(self):
        self.is_leaf = False

class Trie:
    '''
    >>> keys = ["the", "a", "there", "answer", "any", "by", "bye", "their", "abc"]
    >>> trie = Trie()
    >>> for key in keys:
    ...     trie.insert(key)
    >>> print(trie.get_str(trie.root, []))
    ['a', 'abc', 'answer', 'any', 'by', 'bye', 'the', 'their', 'there']
    '''
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        if not word:
            return None

        level = 0
        current_node = self.root

        for char in word:
            char_index = ord(char.lower()) - ord('a')
            if current_node.children[char_index] is None:
                new_node = TrieNode(char.lower())
                current_node.children[char_index] = new_node
                current_node = new_node
            else:
                current_node = current_node.children[char_index]
            level += 1

        current_node.mark_as_leaf()

    def search(self, word):
        pass

    def delete(self, word):
        pass

    def get_str(self, node, lst, prefix='', level=0):
        for child in node.children:
            if child is None:
                continue
            prefix = prefix[:level] + child.char
            if child.is_leaf:
                lst.append(prefix)
            lst = self.get_str(child, lst, prefix, level+1)
        return lst
