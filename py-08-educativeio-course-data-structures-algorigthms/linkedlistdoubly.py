class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList():
    '''
    >>> dll = DoublyLinkedList()
    >>> dll.append(2)
    >>> dll.append(3)
    >>> dll.append(5)
    >>> dll.append(8)
    >>> dll.print_list()
    2 3 5 8
    >>> dll.prepend(1)
    >>> dll.print_list()
    1 2 3 5 8
    >>> dll.insert_after_node(5, 6)
    >>> dll.print_list()
    1 2 3 5 6 8
    >>> dll.insert_after_node(1, 4)
    >>> dll.print_list()
    1 4 2 3 5 6 8
    >>> dll.insert_after_node(8, 9)
    >>> dll.print_list()
    1 4 2 3 5 6 8 9
    >>> dll.insert_before_node(5, 4)
    >>> dll.print_list()
    1 4 2 3 4 5 6 8 9
    '''
    def __init__(self):
        self.head = None


    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current


    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node


    def insert_after_node(self, key, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return None

        current = self.head
        while current and current.data != key:
            current = current.next
        new_node.next = current.next
        new_node.prev = current
        current.next = new_node
        current.next.prev = new_node


    def insert_before_node(self, key, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return None

        current = self.head
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        new_node.next = current
        new_node.prev = prev
        prev.next = new_node
        current.prev = new_node


    def print_list(self):
        if self.head is None:
            return None
        current = self.head
        while current.next:
            print(current.data, end=' ')
            current = current.next
        print(current.data)
