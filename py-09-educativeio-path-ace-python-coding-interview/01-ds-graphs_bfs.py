class MyStack:
    def __init__(self):
        self.stack_list = []

    def is_empty(self):
        return self.size() == 0

    def top(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack_list.pop()


class MyQueue:
    def __init__(self):
        self.queue_list = []

    def is_empty(self):
        return len(self.queue_list) == 0

    def front(self):
        if self.is_empty():
            return None
        return self.queue_list[0]

    def back(self):
        if self.is_empty():
            return None
        return self.queue_list[-1]

    def enqueue(self, value):
        self.queue_list.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        front = self.front()
        self.queue_list.remove(self.front())
        return front


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    '''
    >>> llist = LinkedList()
    >>> llist.insert_at_tail(10)
    >>> llist.insert_at_tail(11)
    >>> llist.insert_at_tail(12)
    >>> llist.insert_at_tail(13)
    >>> llist.insert_at_tail(14)
    >>> llist.insert_at_tail(15)
    >>> llist.print_list()
    10->11->12->13->14->15->None
    >>> llist.delete_tail()
    True
    >>> llist.print_list()
    10->11->12->13->14->None
    >>> llist.delete_head()
    True
    >>> llist.print_list()
    11->12->13->14->None
    >>> llist.delete(12)
    True
    >>> llist.print_list()
    11->13->14->None
    >>> llist.delete(9)
    False
    >>> llist.delete(11)
    True
    >>> llist.print_list()
    13->14->None
    >>> llist.insert_at_tail(14)
    >>> llist.remove_duplicates()
    >>> llist.print_list()
    13->14->None
    '''

    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def is_empty(self):
        return self.head is None

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return self.head

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return

        current = self.head
        prev = None
        while current is not None:
            prev = current
            current = current.next
        prev.next = new_node

    def length(self):
        if self.is_empty():
            return 0

        current = self.head
        length = 0
        while current.next is not None:
            length += 1
            current = current.next

        return length

    def print_list(self):
        if self.is_empty():
            print('List is empty')

        current = self.head
        while current is not None:
            print(f'{current.data}', end='->')
            current = current.next
        print(f'None')

    def delete_head(self):
        if self.is_empty():
            print('List is empty')
            return False

        current = self.head
        self.head = current.next
        current = None
        return True

    def delete_tail(self):
        if self.is_empty():
            print('List is empty')
            return False

        current = self.head
        prev = None
        while current.next is not None:
            prev = current
            current = current.next
        prev.next = None
        return True

    def delete(self, value):
        if self.is_empty():
            print('List is empty')
            return False

        current = self.head
        if self.head.data == value:
            self.head = current.next
            return True

        prev = None
        while current.data != value and current.next is not None:
            prev = current
            current = current.next

        if current is not None and current.data == value:
            prev.next = current.next
            current = None
            return True

        return False

    def search(self, value):
        if self.is_empty():
            return ('List is empty')
            return None

        current = self.head
        while current is not None:
            if current.data == value:
                return current
            current = current.next

        return None

    def remove_duplicates(self):
        if self.is_empty():
            return

        # If list only has one node, leave it unchanged
        if self.head.next is None:
            return

        outer_node = self.head
        while outer_node:
            inner_node = outer_node  # Iterator for the inner loop
            while inner_node:
                if inner_node.next:
                    if outer_node.data == inner_node.next.data:
                        # Duplicate found, so now removing it
                        new_next = inner_node.next.next
                        inner_node.next = new_next
                    else:
                        # Otherwise simply iterate ahead
                        inner_node = inner_node.next
                else:
                    # Otherwise simply iterate ahead
                    inner_node = inner_node.next
            outer_node = outer_node.next
        return


class Graph:
    '''
    >>> g = Graph(4)
    >>> g.add_edge(0, 1)
    >>> g.add_edge(1, 2)
    >>> g.add_edge(0, 3)
    >>> g.add_edge(3, 2)
    >>> g.print_graph()
    True
    '''

    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.array = []
        for i in range(num_vertices):
            llist = LinkedList()
            self.array.append(llist)

    def add_edge(self, source, destination):
        if (source < self.num_vertices and destination < self.num_vertices):
            self.array[source].insert_at_head(destination)
        # If we were to implement an Undirected Graph i.e (1,0) == (0,1)
        # We would create an edge from destination towards source as well
        # i.e self.array[destination].insert_at_head(source)

    def print_graph(self):
        print(">>Adjacency List of Directed Graph<<")
        for i in range(self.num_vertices):
            print("|", i, end=" | => ")
            temp = self.array[i].get_head()
            while(temp is not None):
                print("[", temp.data, end=" ] -> ")
                temp = temp.next
            print("None")


def bfs_traversal_helper(g, source, visited):
    result = ""
    queue = MyQueue()
    queue.enqueue(source)

    visited[source] = True
    while(queue.is_empty() is False):
        current_node = queue.dequeue()
        result += str(current_node)

        temp = g.array[current_node].head
        while (temp is not None):
            if(visited[temp.data] is False):
                queue.enqueue(temp.data)
                visited[temp.data] = True
            temp = temp.next

    return result, visited


def bfs_traversal(g, source):
    result = ""
    n_vertices = g.num_vertices
    if n_vertices == 0:
        return result

    # A list to hold the history of visited nodes
    # Make a node visited whenever you enqueue it into queue
    visited = []
    for i in range(n_vertices):
        visited.append(False)

    # Start from source
    result, visited = bfs_traversal_helper(g, source, visited)

    # visit remaining nodes
    for i in range(n_vertices):
        if visited[i] is False:
            result_new, visited = bfs_traversal_helper(g, i, visited)
            result += result_new
    return result


g = Graph(4)
n_vertices = g.num_vertices

if(n_vertices == 0):
    print("Graph is empty")
elif(n_vertices < 0):
    print("Graph cannot have negative vertices")
else:
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)

    print(bfs_traversal(g, 0))
