import timeit
import unittest
from random import randint


class MyStack:
    def __init__(self):
        self.stack = []
        self.max_values = [] # find_max optim
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def push(self, obj):
        self.stack.append(obj)
        if (len(self.max_values) == 0) or (obj > self.max_values[-1]):
            self.max_values.append(obj)
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.stack[-1]
    
    def pop(self):
        if self.isEmpty():
            return None
        
        popped = self.stack.pop()
        if (popped == self.max_values[-1]) and (not popped in self.stack):
            self.max_values.pop()

        return popped
    
    def reverse(self):
        reversed = MyStack()

        if self.isEmpty():
            return reversed
        
        i = len(self.stack) - 1
        while i >= 0:
            reversed.push(self.stack.pop())
            i -= 1
        return reversed
    
    def find_max(self):
        if self.isEmpty():
            return None
        return self.max_values[-1]
    
    def size(self):
        return len(self.stack)
    
    def __str__(self):
        if self.isEmpty():
            return ''
        
        s = str(self.stack[0])
        for obj in self.stack[1:]:
            s += ' '
            s += str(obj)
        return s

class TestMyStack(unittest.TestCase):
    
    def test_push_in_empty_stack(self):
        myStack = MyStack()
        myStack.push(5)
        actual = myStack.stack
        expected = [5]
        self.assertEqual(actual, expected, msg='test_push_in_empty_stack')
    
    def test_push_in_non_empty_stack(self):
        myStack = MyStack()
        myStack.push(4)
        myStack.push(5)
        myStack.push(6)
        myStack.push(7)
        actual = myStack.stack
        expected = [4, 5, 6, 7]
        self.assertEqual(actual, expected, msg='test_push_in_non_empty_stack')
    
    def test_pop_from_empty_stack(self):
        myStack = MyStack()
        actual = myStack.pop()
        expected = None
        self.assertEqual(actual, expected, msg='test_pop_from_empty_stack')
    
    def test_pop_from_non_empty_stack(self):
        myStack = MyStack()
        myStack.push(4)
        myStack.push(5)
        myStack.push(6)
        myStack.push(7)
        actual_value = myStack.pop()
        expected_value = 7
        actual_stack = myStack.stack
        expected_stack = [4, 5, 6]
        self.assertEqual(actual_value, expected_value, msg='test_pop_from_non_empty_stack (value)') \
            and self.assertEqual(actual_stack, expected_stack, msg='test_pop_from_non_empty_stack (stack)')
    
    def test_peek_in_empty_stack(self):
        myStack = MyStack()
        actual = myStack.pop()
        expected = None
        self.assertEqual(actual, expected, msg='test_peek_in_empty_stack')
    
    def test_peek_in_non_empty_stack(self):
        myStack = MyStack()
        myStack.push(4)
        myStack.push(5)
        myStack.push(6)
        myStack.push(7)
        actual_value = myStack.peek()
        expected_value = 7
        actual_stack = myStack.stack
        expected_stack = [4, 5, 6, 7]
        self.assertEqual(actual_value, expected_value, msg='test_peek_in_non_empty_stack (value)') \
            and self.assertEqual(actual_stack, expected_stack, msg='test_peek_in_non_empty_stack (stack)')
    
    def test_reverse_non_empty_stack(self):
        myStack = MyStack()
        myStack.push(4)
        myStack.push(5)
        myStack.push(6)
        myStack.push(7)
        reversed = myStack.reverse()
        actual_value = reversed.stack
        expected_value = [7, 6, 5, 4]
        self.assertEqual(actual_value, expected_value, msg='test_reverse_non_empty_stack')
    
    def test_reverse_empty_stack(self):
        myStack = MyStack()
        reversed = myStack.reverse()
        actual_value = reversed.stack
        expected_value = []
        self.assertEqual(actual_value, expected_value, msg='test_reverse_empty_stack')

if __name__ == '__main__':
    # unittest.main(verbosity=2)
    myStack = MyStack()
    size = 1000000
    range_values = 900000000

    starttime = timeit.default_timer()
    values = [randint(0, range_values) for i in list(range(0, size))]
    endtime = timeit.default_timer()
    duration = endtime - starttime
    print('timeit: generating {} random values up to {} takes {}'.format(size, range_values, duration))

    starttime = timeit.default_timer()
    for value in values:
        myStack.push(value)
    endtime = timeit.default_timer()
    duration = endtime - starttime
    print('timeit: MyStack.push()     {} times takes {}'.format(size, duration))

    starttime = timeit.default_timer()
    for i in list(range(myStack.size())):
        myStack.pop()
    endtime = timeit.default_timer()
    duration = endtime - starttime
    print('timeit: MyStack.pop()      {} times takes {}'.format(size, duration))

    starttime = timeit.default_timer()
    for i in list(range(myStack.size())):
        myStack.peek()
    endtime = timeit.default_timer()
    duration = endtime - starttime
    print('timeit: MyStack.peek()     {} times takes {}'.format(size, duration))

    starttime = timeit.default_timer()
    for i in list(range(myStack.size())):
        myStack.find_max()
    endtime = timeit.default_timer()
    duration = endtime - starttime
    print('timeit: MyStack.find_max() {} times takes {}'.format(size, duration))
