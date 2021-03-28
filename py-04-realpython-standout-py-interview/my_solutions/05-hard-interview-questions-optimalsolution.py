from collections import defaultdict, Counter


class Link:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        if not self.next:
            return f'Link({self.val})'
        return f'Link({self.val}, {self.next})'

    def append(self, link):
        if self is None or self.val is None:
            self.val = link.val
            self.next = None
        else:
            last = self
            while last.next:
                last = last.next
            last.next = link

    def append_value(self, val):
        if self is None or self.val is None:
            self.val = val
            self.next = None
        else:
            last = self
            while last.next:
                last = last.next
            last.next = Link(val)


def merge_k_linked_lists(linked_lists):
    '''
    Merge k sorted linked lists into one sorted linked list.
    k - number of linked lists
    n - max length of any linked list
    k*n - number of unique values in all linked lists

    >>> print(merge_k_linked_lists([
    ...     Link(1, Link(2)),
    ...     Link(3, Link(4))
    ...     ]))
    Link(1, Link(2, Link(3, Link(4))))

    >>> print(merge_k_linked_lists([
    ...     Link(1, Link(2)),
    ...     Link(2, Link(4)),
    ...     Link(3, Link(3))
    ...     ]))
    Link(1, Link(2, Link(2, Link(3, Link(3, Link(4))))))

    >>> print(merge_k_linked_lists([Link(1, Link(2))]))
    Link(1, Link(2))

    >>> print(merge_k_linked_lists([]))
    None
    '''

    # METHOD:
    # Create a mapping {value:[nodes]} in the linked lists
    # Sort the mapping's keys
    # Insert the nodes into the result linked list

    if len(linked_lists) == 0:
        return None

    if len(linked_lists) == 1:
        return linked_lists[0]

    # Create a mapping of values to nodes.
    # Output: {value: Link}
    # Time: O(k*n)
    values_to_nodes = defaultdict(Link)
    for llist in linked_lists:  # O(k)
        while llist is not None:  # O(n)
            values_to_nodes[llist.val].append_value(llist.val)
            llist = llist.next

    # Sort the dictionary's entries by keys/values.
    # Output: [(value: [linked_list])]
    # Time: O(k*n log(k*n))
    sorted_vals = sorted(values_to_nodes.items(), key=lambda x: x[0])

    # Insert the nodes into the result linked list.
    # Time: O(k*n)
    result = sorted_vals[0][1]
    for value, llist in sorted_vals[1:]:
        result.append(llist)

    # runtime: O(k*n)
    return result
