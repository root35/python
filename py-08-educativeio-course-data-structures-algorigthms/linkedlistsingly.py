from collections import defaultdict

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SinglyLinkedList():
    '''
    >>> sll = SinglyLinkedList()

    >>> sll.append(5)
    >>> print(str(sll))
    5
    >>> sll.append(8)
    >>> sll.append(13)
    >>> print(str(sll))
    5 8 13

    >>> sll.prepend(0)
    >>> print(str(sll))
    0 5 8 13

    >>> sll.insert_after_node(8, 9)
    >>> print(str(sll))
    0 5 8 9 13
    >>> sll.insert_after_node(13, 21)
    >>> print(str(sll))
    0 5 8 9 13 21

    >>> sll.delete_node(13)
    >>> print(str(sll))
    0 5 8 9 21
    >>> sll.delete_node(0)
    >>> print(str(sll))
    5 8 9 21
    >>> sll.delete_node(21)
    >>> print(str(sll))
    5 8 9

    >>> sll.append(3)
    >>> sll.append(4)
    >>> sll.delete_node_at_position(2)
    >>> print(str(sll))
    5 8 3 4
    >>> sll.delete_node_at_position(0)
    >>> print(str(sll))
    8 3 4
    >>> sll.delete_node_at_position(2)
    >>> print(str(sll))
    8 3
    >>> sll.delete_node_at_position(3)
    >>> print(str(sll))
    8 3

    >>> sll.length(sll.head)
    2

    >>> sll.append(11)
    >>> sll.append(12)
    >>> sll.append(13)
    >>> print(str(sll))
    8 3 11 12 13
    >>> sll.swap_nodes(3, 13)
    >>> print(str(sll))
    8 13 11 12 3
    >>> sll.swap_nodes(8, 3)
    >>> print(str(sll))
    3 13 11 12 8
    >>> sll.swap_nodes(13, 12)
    >>> print(str(sll))
    3 12 11 13 8
    >>> sll.swap_nodes(13, 21)
    >>> print(str(sll))
    3 12 11 13 8

    >>> reversed_sll = sll.reverse()
    >>> print(str(reversed_sll))
    8 13 11 12 3

    >>> a_sll = SinglyLinkedList()
    >>> a_sll.append(1)
    >>> a_sll.append(2)
    >>> a_sll.append(10)
    >>> a_sll.append(21)
    >>> b_sll = SinglyLinkedList()
    >>> b_sll.append(3)
    >>> b_sll.append(4)
    >>> b_sll.append(5)
    >>> b_sll.append(19)
    >>> b_sll.append(24)
    >>> b_sll.append(42)
    >>> a_sll.merge_sorted(b_sll)
    >>> print(str(a_sll))
    1 2 3 4 5 10 19 21 24 42

    >>> a_sll.append(10)
    >>> a_sll.append(1)
    >>> a_sll.append(21)
    >>> a_sll.remove_duplicates()
    >>> print(str(a_sll))
    1 2 3 4 5 10 19 21 24 42
    '''

    def __init__(self):
        self.head = None


    def append(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            return

        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = new_node


    def prepend(self, data):
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head


    def insert_after_node(self, prev_node, data):
        new_node = Node(data)
        pointer = self.head
        while pointer.next and pointer.data != prev_node:
            pointer = pointer.next
        new_node.next = pointer.next
        pointer.next = new_node


    def delete_node(self, data):
        if self.is_empty():
            return None

        current_node = self.head
        if current_node.data == data:
            self.head = self.head.next
            current_node = None
            return

        prev = self.head
        current = self.head.next
        while current:
            if current.data == data:
                prev.next = current.next
                current = current.next
            else:
                prev = prev.next
                current = current.next


    def delete_node_at_position(self, position):
        if self.is_empty():
            return None

        if position == 0:
            self.head = self.head.next
            return None

        current = self.head
        prev = None
        i = 0
        while current and i < position:
            prev = current
            current = current.next
            i += 1

        if current is None:
            return None
        prev.next = current.next
        current = None


    def swap_nodes(self, data1, data2):
        if (data1 == data2) or (self.length(self.head) <= 1):
            return None

        prev1 = None
        current1 = self.head
        while current1 and current1.data != data1:
            prev1 = current1
            current1 = current1.next

        prev2 = None
        current2 = self.head
        while current2 and current2.data != data2:
            prev2 = current2
            current2 = current2.next

        if current1 is None or current2 is None:
            return

        if prev1:
            prev1.next = current2
        else:
            self.head = current2

        if prev2:
            prev2.next = current1
        else:
            self.head = current2

        current1.next, current2.next = current2.next, current1.next


    def reverse(self):
        if self.length(self.head) <= 1:
            return self

        current = self.head
        data = list()
        while current:
            data.append(current.data)
            current = current.next

        reversed_llist = SinglyLinkedList()
        for i in range(len(data) - 1, -1, -1):
            reversed_llist.append(data[i])

        return reversed_llist


    def merge_sorted(self, llist):
        if not self:
            return llist
        if not llist:
            return self

        s_current = self.head
        l_current = llist.head
        q = new_head = None

        if s_current.data <= l_current.data:
            new_head = s_current
            s_current = s_current.next
        else:
            new_head = l_current
            l_current = l_current.next

        q = new_head

        while s_current and l_current:
            if s_current.data < l_current.data:
                q.next = s_current
                q = q.next
                s_current = s_current.next
            elif l_current.data < s_current.data:
                q.next = l_current
                q = q.next
                l_current = l_current.next
            elif s_current.data == l_current.data:
                q.next = s_current
                q = q.next
                q.next = l_current
                q = q.next
                s_current = s_current.next
                l_current = l_current.next
                print('-')

        if s_current:
            q.next = s_current
        elif l_current:
            q.next = l_current

        self.head = new_head


    def remove_duplicates(self):
        if self.length(self.head) <= 1:
            return None

        keys = list()
        current = self.head
        prev = None

        while current:
            if current.data not in keys:
                keys.append(current.data)
                prev = current
                current = current.next
            else:
                prev.next = current.next
                current = current.next


    def length(self, node):
        if node is None:
            return 0
        return 1 + self.length(node.next)


    def is_empty(self):
        return self.head is None


    def __str__(self):
        tail = self.head
        repr = str(tail.data)
        while tail.next:
            tail = tail.next
            repr += ' ' + str(tail.data)
        return repr
