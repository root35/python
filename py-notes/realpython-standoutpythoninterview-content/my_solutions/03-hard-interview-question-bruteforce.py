class Link:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if not self.next:
            return f'Link({self.val})'
        return f'Link({self.val}, {self.next})'


def merge_k_linked_lists(linked_lists):
    '''
    Merge k sorted linked lists into one sorted linked list.
    k - number of linked lists
    n - max length of any linked list

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
    if len(linked_lists) == 0:
        return None

    if len(linked_lists) == 1:
        return linked_lists[0]

    # STEP 1: Concatenate the linked lists

    merged = linked_lists[0]
    next = merged.next

    # O(k*n)
    for llist in linked_lists[1:]:
        next.next = llist
        next = llist.next

    # STEP 2: Sort the complete linked list
    # Compare each current_node with each following_node in the list,
    # and inverse values if following_node.value > current_node.value

    node = merged

    # O(n*n)
    while node.next is not None:
        current_val = node.val
        current_node = node

        while current_node.next is not None:
            if current_val > current_node.val:
                node.val, current_node.val = current_node.val, node.val
            current_node = current_node.next
        if current_val > current_node.val:
            node.val, current_node.val = current_node.val, node.val

        node = node.next

    return merged
