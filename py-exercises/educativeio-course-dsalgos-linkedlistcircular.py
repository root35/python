class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class CircularLinkedList():
    '''
    >>> cll = CircularLinkedList()
    >>> print(cll.is_empty())
    True

    >>> cll.append(2)
    >>> cll.append(4)
    >>> cll.append(6)
    >>> cll.append(8)
    >>> cll.append(10)
    >>> cll.append(12)
    >>> cll.print_cll()
    2 4 6 8 10 12

    >>> cll.prepend(1)
    >>> cll.print_cll()
    1 2 4 6 8 10 12

    >>> cll.remove(4)
    >>> cll.print_cll()
    1 2 6 8 10 12
    >>> cll.remove(12)
    >>> cll.print_cll()
    1 2 6 8 10
    >>> cll.remove(1)
    >>> cll.print_cll()
    2 6 8 10

    >>> len(cll)
    4

    >>> a, b = cll.split_half()
    >>> a.print_cll()
    2 6
    >>> b.print_cll()
    8 10

    >>> c, d = a.split_half()
    >>> c.print_cll()
    2
    >>> d.print_cll()
    6
    '''
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.head.next = self.head
            return None

        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head


    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.head.next = self.head
            return None

        new_node.next = self.head
        current = self.head
        while current:
            if current.next == self.head:
                break
            current = current.next
        current.next = new_node
        self.head = new_node


    def remove(self, data):
        if self.head is None:
            return None

        current = self.head
        prev = None

        if self.head.data == data:
            while current.next != self.head:
                current = current.next
            self.head = self.head.next
            current.next = self.head

        else:
            while current.data != data:
                prev = current
                current = current.next
                if current.next == self.head:
                    break

            if current.data == data:
                if current.next == self.head:
                    prev.next = self.head
                else:
                    prev.next = current.next


    def split_half(self):
        length = len(self)
        if length == 0:
            return None
        if length == 1:
            return self.head

        mid = length // 2
        count = 0

        current = self.head
        prev = None
        while count < mid:
            prev = current
            current = current.next
            count += 1

        prev.next = self.head

        second = CircularLinkedList()
        second.head = current
        while current:
            if current.next == self.head:
                break
            current = current.next
        current.next = second.head

        return self, second

#   2 | 6 7>2
# prev: 4
# current: 6


    def __len__(self):
        if self.head is None:
            return 0

        count = 0
        current = self.head
        while current:
            count += 1
            if current.next == self.head:
                break
            current = current.next

        return count


    def is_empty(self):
        return self.head is None


    def print_cll(self):
        if self.is_empty():
            return None

        current = self.head
        print(str(current.data), end='')
        current = current.next
        while current != self.head:
            print(' ' + str(current.data), end='')
            current = current.next
