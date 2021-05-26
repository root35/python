## -- EASY

# You are given the root of a binary tree where each node has a value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

# For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

# Return the sum of these numbers. The answer is guaranteed to fit in a 32-bits integer.
# Example 1:

# Input: root = [1,0,1,0,1,0,1]
# Output: 22
# Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
# Example 2:

# Input: root = [0]
# Output: 0
# Example 3:

# Input: root = [1]
# Output: 1
# Example 4:

# Input: root = [1,1]
# Output: 3







# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        sum = 0
        bin_nums = self.get_pathes(root, [])
        for bin_num in bin_nums:
            sum += self.convert_binary_to_decimal(int(bin_num))
        return sum

    def get_pathes(self, node, lst, prefix='', level=0):
        if node is not None:
            prefix = prefix[:level] + str(node.val)
            if self.is_leaf(node):
                lst.append(prefix)
            else:
                if node.left is not None:
                    lst = self.get_pathes(node.left, lst, prefix, level+1)
                if node.right is not None:
                    lst = self.get_pathes(node.right, lst, prefix, level+1)
        return lst

    def is_leaf(self, node):
        return node.left is None and node.right is None

    def convert_binary_to_decimal(self, num: int) -> int:
        decimal_value = 0
        pos = 0
        while num > 0:
            last_digit = num % 10
            num = num // 10
            decimal_value += pow(2, pos) * last_digit
            pos += 1
        return decimal_value








## -- MEDIUM (Synonymous sentences)

# Given a list of pairs of equivalent words synonyms and a sentence text, Return all possible synonymous sentences sorted lexicographically.


# Example 1:

# Input:
# synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]],
# text = "I am happy today but was sad yesterday"
# Output:
# ["I am cheerful today but was sad yesterday",
# "I am cheerful today but was sorrow yesterday",
# "I am happy today but was sad yesterday",
# "I am happy today but was sorrow yesterday",
# "I am joy today but was sad yesterday",
# "I am joy today but was sorrow yesterday"]
# Example 2:

# Input: synonyms = [["happy","joy"],["cheerful","glad"]], text = "I am happy today but was sad yesterday"
# Output: ["I am happy today but was sad yesterday","I am joy today but was sad yesterday"]
# Example 3:

# Input: synonyms = [["a","b"],["c","d"],["e","f"]], text = "a c e"
# Output: ["a c e","a c f","a d e","a d f","b c e","b c f","b d e","b d f"]
# Example 4:

# Input: synonyms = [["a","QrbCl"]], text = "d QrbCl ya ya NjZQ"
# Output: ["d QrbCl ya ya NjZQ","d a ya ya NjZQ"]






import itertools
from string import Template

class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        lex = [s for sublist in synonyms for s in sublist]
        merged_syns = self.merge_intersected_lists(synonyms)
        combinations = list(itertools.product(*merged_syns))

        tokens = text.split(' ')
        templ = ''
        num_syns = 0
        for token in tokens:
            if token in lex:
                templ += ' $s' + str(num_syns)
                num_syns += 1
            else:
                templ += ' ' + token
        template = Template(templ.strip())

        sents = list()
        for comb in combinations:
            template_dict = defaultdict(str)
            for i, elem in enumerate(comb):
                template_dict['s' + str(i)] = elem
            sent = template.substitute(**template_dict)
            if sent not in sents:
                sents.append(sent)

        return sorted(sents)

    def merge_intersected_lists(self, lists):
        visited = []
        merged_lists = list()
        for i, lst1 in enumerate(lists):
            if i in visited:
                continue
            merged = False
            for j, lst2 in enumerate(lists[i+1:], start=i+1):
                if j in visited:
                    continue
                if self.intersect_lists(lst1, lst2) is True:
                    merged = list(set(lst1 + lst2))
                    merged_lists.append(sorted(merged))
                    visited.append(j)
                    merged = True
            if merged is False:
                merged_lists.append(lst1)
        return merged_lists

    def intersect_lists(self, lst1, lst2):
        for elem in lst1:
            if elem in lst2:
                return True
        return False

