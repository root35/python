class MaxHeap:
    '''
    Heap properties:
    - Max heap: parent >= childs (root always contains the max key)
      Min heap: parent <= childs (root always contains the min key)

    - List representation = more space efficient
      - all parent nodes are in first half of the list:
         index <= floor( (n-1) / 2
      - for node at k-th index:
        - left child : 2k+1
        - right child: 2k+2
        - parent     : floor((k - 1) / 2)

    - Insert: O(logn)
      Delete: O(logn)
      Search: O(n)

    >>> heap = MaxHeap()
    >>> heap.insert(12)
    >>> heap.insert(10)
    >>> heap.insert(-10)
    >>> heap.insert(100)
    >>> print(heap.get_max())
    100

    >>> max_heap_lst = [9, 4, 7, 1, -2, 6, 5]
    >>> max_heap = MaxHeap()
    >>> print(max_heap.convert_to_min_heap(max_heap_lst))
    [-2, 1, 5, 9, 4, 6, 7]
    >>> k_largest(3, max_heap_lst)
    [9, 7, 6]
    '''
    def __init__(self):
        self.heap = list()

    def insert(self, value):
        '''
        - Create a new child node at the end of the heap
        - Place the new key at that node
        - Then, restore the heap property by swapping parent
        and child values if the parent key is smaller than
        the child key. We call this ‘percolating up’.
        - Continue to percolate up until the heap property is restored.

        O(logn)
        '''
        self.heap.append(value)
        self.__percolate_up(len(self.heap) - 1)

    def get_max(self):
        ''' O(1) '''
        if self.heap:
            return self.heap[0]
        return None

    def remove_max(self):
        '''
        - Delete the root node
        - Move the key of last child node at last level to the root
        - Now compare the key with its children and if the key is
        smaller than the key at any of the child nodes, swap values.
        We call this ‘max heapifying.’
        - Continue to max heapify until the heap property is restored.

        O(log(n))
        '''
        if len(self.heap) > 1:
            max = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self.__max_heapify(0)
            return max
        elif len(self.heap) == 1:
            max = self.heap[0]
            del self.heap[0]
            return max
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
        elif self.heap[parent] < self.heap[index]:
            current = self.heap[parent]
            self.heap[parent] = self.heap[index]
            self.heap[index] = current
            self.__percolate_up(parent)

    def __max_heapify(self, index):
        '''
        Restore the heap property after a node is removed.
        Swap values of the parent nodes with values of their largest
        child nodes until min/max heap property is restored.

        O(log(n))
        '''
        left = (index * 2) + 1
        right = (index * 2) + 2
        largest = index

        # check if left child exists and is less than smallest
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left

        # check if right child exists and is less than smallest
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right

        # check if current index is not the smallest
        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self.__max_heapify(largest)

    def build_heap(self, max_heap_lst):
        '''
        Number of comparisons for a particular node at height h is O(h).
        '''
        self.heap = max_heap_lst
        for i in range(len(max_heap_lst) - 1, -1, -1):
            self.__max_heapify(i)

    def convert_to_min_heap(self, max_heap_lst):
        '''
        Example input: [9,4,7,1,-2,6,5] -> output: [-2,1,5,9,4,6,7]

        O(n)
        '''
        for i in range(len(max_heap_lst), -1, -1):
            max_heap_lst = self.__convert_to_min_heap_helper(max_heap_lst, i)
        return max_heap_lst

    def __convert_to_min_heap_helper(self, heap, index):
        left_idx = (index * 2) + 1
        right_idx = (index * 2) + 2
        smallest_idx = index

        # check if left child exists and is less than smallest
        if len(heap) > left_idx and heap[smallest_idx] > heap[left_idx]:
            smallest_idx = left_idx

        # check if right child exists and is less than smallest
        if len(heap) > right_idx and heap[smallest_idx] > heap[right_idx]:
            smallest_idx = right_idx

        # check if current index is not the smallest
        if smallest_idx != index:
            # swap current index value with smallest
            heap[smallest_idx], heap[index] = heap[index], heap[smallest_idx]
            # min heapify the new node
            self.__convert_to_min_heap_helper(heap, smallest_idx)

        return heap


def k_largest(k, lst):
    '''
    O(k logn)
    '''
    max_heap = MaxHeap()
    max_heap.build_heap(lst)
    k_largest = [max_heap.remove_max() for i in range(k)]
    return k_largest

