class MinHeap:
    '''
    Heap properties:
    - Max heap: parent >= childs (root always contains the max key)
      Min heap: parent <= childs (root always contains the min key)

    - List representation = more space efficient
      - all parent nodes are in first half of the list:
         index <= floor( (n-1) / 2
      - index 2k+1 = left child of node at kth index
      - index 2k+2 = right child of node at kth index
      - index floor((k - 1) / 2) = parent node of at kth index

    >>> heap = MinHeap()
    >>> heap.insert(12)
    >>> heap.insert(10)
    >>> heap.insert(-10)
    >>> heap.insert(100)

    >>> print(heap.get_min())
    -10
    >>> print(heap.remove_min())
    -10
    >>> print(heap.get_min())
    10
    >>> heap.insert(-100)
    >>> print(heap.get_min())
    -100
    >>> k_smallest(2, [9, 4, 7, 1, -2, 6, 5])
    [-2, 1]
    '''
    def __init__(self):
        self.heap = list()

    def insert(self, value):
        '''
        - Create a new child node at the end of the heap
        - Place the new key at that node (append it to list or array)
        - Percolate up until you reach the root node and the heap

        property is satisfied
        O(logn)
        '''
        self.heap.append(value)
        self.__percolate_up(len(self.heap) - 1)

    def get_min(self):
        ''' O(1) '''
        if self.heap:
            return self.heap[0]
        return None

    def remove_min(self):
        '''
        - Delete the root node
        - Move the key of the last child node to root
        - Perculate down: if the key is larger than the key at any
        of the child nodes, swap values
        - Repeat until you reach the last node

        O(log(n))
        '''
        if len(self.heap) > 1:
            min = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self.__min_heapify(0)
            return min
        elif len(self.heap) == 1:
            min = self.heap[0]
            del self.heap[0]
            return min
        return None

    def __percolate_up(self, index):
        '''
        Swapp value at a parent node if it is less than value at a
        child node.
        Function is called recursively on each parent node until
        the root is reached.

        O(log(n))
        '''
        parent = (index - 1) // 2
        if index <= 0:
            return None
        elif self.heap[parent] > self.heap[index]:
            current = self.heap[parent]
            self.heap[parent] = self.heap[index]
            self.heap[index] = current
            self.__percolate_up(parent)

    def __min_heapify(self, index):
        '''
        Restore the heap property after a node is removed.
        Swap values of the parent nodes with values of their largest
        child nodes until min/max heap property is restored.

        O(log(n))
        '''
        left = (index * 2) + 1
        right = (index * 2) + 2
        smallest = index

        # check if left child exists and is less than smallest
        if len(self.heap) > left and self.heap[smallest] > self.heap[left]:
            smallest = left

        # check if right child exists and is less than smallest
        if len(self.heap) > right and self.heap[smallest] > self.heap[right]:
            smallest = right

        # check if current index is not the smallest
        if smallest != index:
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self.__min_heapify(smallest)

    def build_heap(self, heap_array):
        '''
        Number of comparisons for a particular node at height h is O(h).
        '''
        self.heap = heap_array
        for i in range(len(heap_array) - 1, -1, -1):
            self.__min_heapify(i)


def k_smallest(k, lst):
    '''
    O(k logn)
    '''
    min_heap = MinHeap()
    min_heap.build_heap(lst)
    k_smallest = [min_heap.remove_min() for i in range(k)]
    return k_smallest
