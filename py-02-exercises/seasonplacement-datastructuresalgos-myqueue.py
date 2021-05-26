import unittest

class MyQueue:
    def __init__(self):
        self.queue = []
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def push(self, obj):
        self.queue.append(obj)
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.queue[-1]
    
    def pop(self):
        if self.isEmpty():
            return None
        return self.queue.pop()
    
    def __str__(self):
        if self.isEmpty():
            return ''

        s = str(self.queue[0])
        for item in self.queue[1:]:
            s += ' '
            s += str(item)
        return s

class TestMyQueue(unittest.TestCase):
    
    def test_push_in_empty_queue(self):
        myQueue = MyQueue()
        myQueue.push(5)
        actual = myQueue.queue
        expected = [5]
        self.assertEqual(actual, expected, msg='test_push_in_empty_queue')
    
    def test_push_in_non_empty_queue(self):
        myQueue = MyQueue()
        myQueue.push(5)
        myQueue.push(8)
        myQueue.push(13)
        actual = myQueue.queue
        expected = [5, 8, 13]
        self.assertEqual(actual, expected, msg='test_push_in_non_empty_queue')
    
    def test_pop_from_empty_queue(self):
        myQueue = MyQueue()
        actual = myQueue.pop()
        expected = None
        self.assertEqual(actual, expected, msg='test_pop_from_empty_queue')
    
    def test_pop_from_non_empty_queue(self):
        myQueue = MyQueue()
        myQueue.push(5)
        myQueue.push(8)
        myQueue.push(13)
        actual_value = myQueue.pop()
        expected_value = 13
        actual_stack = myQueue.queue
        expected_stack = [5, 8]
        self.assertEqual(actual_value, expected_value, msg='test_pop_from_non_empty_queue (value)') \
            and self.assertEqual(actual_stack, expected_stack, msg='test_pop_from_non_empty_queue (queue)')
    
    def test_peek_in_empty_queue(self):
        myQueue = MyQueue()
        actual = myQueue.pop()
        expected = None
        self.assertEqual(actual, expected, msg='test_pop_from_empty_queue')
    
    def test_peek_in_non_empty_queue(self):
        myQueue = MyQueue()
        myQueue.push(5)
        myQueue.push(8)
        myQueue.push(13)
        actual_value = myQueue.pop()
        expected_value = 13
        actual_queue = myQueue.queue
        expected_queue = [5, 8, 13]
        self.assertEqual(actual_value, expected_value, msg='test_pop_from_non_empty_queue (value)') \
            and self.assertEqual(actual_queue, expected_queue, msg='test_pop_from_non_empty_queue (queue)')

if __name__ == '__main__':
    unittest.main(verbosity=2)
