
class MyQueue:

    def __init__(self):
        self.queue = []
        self.size = 0
        self.front = -1
        self.rear = -1
    
    def enqueue(self, item):
        if self.isFullSimple() or self.isFullCircular():
            print('Queue is full')
        
        elif (self.isEmpty()):
            self.front = self.rear = 0
            self.queue.append(item)
            print(self.queue)
        
        else:
            self.queue.append(item)
            self.rear += 1
            self.size += 1
    
    # Simple queue
    def isEmpty(self):
        if (self.front == -1) and (self.rear == -1):
            return True
        return False

    def isFullSimple(self):
        print('simple')
        if (self.size > 0) and (self.rear == self.size - 1):
            return True
        return False
    
    def isFullCircular(self):
        """ Circular queue, 2 possible scenarios:
        For example: size = 5
        Normal:   (front = 0 && rear = size-1) -> (4+1) % 5 = 5 % 5 = 0
        Circular: (front = 2 && rear = 1)      -> (1+1) % 5 = 2 % 5 = 2
        """
        print('circular')
        if (self.size > 0) and (((self.rear + 1) % self.size) == self.front):
            return True
        return False
    
    def __str__(self):
        if self.isEmpty():
            return ''

        s = str(self.queue[0])
        i = 1
        while i <= self.rear:
            s += ' '
            s += str(self.queue[i])
            i += 1
        
        return s
    
items = [1, 3, 5]
myQueue = MyQueue()
print(myQueue)
for item in items:
    myQueue.enqueue(item)
print(myQueue)