class Stack:
    '''
    >>> mystack = Stack()
    >>> mystack.push(5)
    >>> mystack.push(1)
    >>> mystack.push(8)
    >>> mystack.peek()
    8
    >>> mystack.pop()
    >>> print(mystack.items)
    [5, 1]
    '''

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if not self.is_empty() else False

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
