class Link:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
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

    # METHOD:
    # Look at the first value of all input linked lists
    # Find the minimum:
    #   insert it in result linked list
    #   "remove" it from its original linked list

    linked_lists_copy = linked_lists[:]  # O(k)
    result = Link(0)
    pointer = result

    # O(k * k*n)
    # while runs k*n times
    while any(linked_lists_copy):  # O(k)

        # Look at the first value of all input linked lists
        front_vals = [llist.val
                      for llist in linked_lists_copy
                      if llist is not None]  # O(k)

        if len(front_vals) == 0:
            break

        # Find the minimum:
        min_val = min(front_vals)  # O(k)

        for i, llist in enumerate(linked_lists_copy):  # O(k)
            if llist is None:
                continue

            if llist.val == min_val:
                # insert the minimum in result linked list
                pointer.next = Link(llist.val)
                pointer = pointer.next

                # "remove" the minimum from the original linked lists
                # Link(1, Link(2)) -> Link(2)
                linked_lists_copy[i] = llist.next

    # Final runtime: O(k *n*k)
    result = result.next
    return result
