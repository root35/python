# Enter your code here. Read input from STDIN. Print output to STDOUT

func_dict = {
    1: lambda queue, obj: queue.push(obj),
    2: lambda queue: queue.pop(),
    3: lambda queue: queue.peek(),
}

class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def isEmpty(self):
        if self.stack2 is None:
            return (len(self.stack1) == 0) and (len(self.stack2) == 0)
    
    def push(self, obj):
        self.stack1.append(obj)
    
    def pop(self):
        if self.isEmpty():
            return None
        
        if len(self.stack2) == 0:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            
        return self.stack2.pop()
    
    def peek(self):
        if self.isEmpty():
            print('')
        elif len(self.stack2) == 0:
            print(self.stack1[0])
        else:
            print(self.stack2[-1])
    
    def __str__(self):
        if self.isEmpty():
            return ''

        s = ' '.join(list(map(str, self.stack1)))
        i = len(self.stack2) - 1
        while i >= 0:
            s += ' '
            s += str(self.stack2[i])

        return s

if __name__ == '__main__':
    n_queries = int(input())
    queries = []
    myQueue = Queue()

    for i in range(n_queries):
        query = list(map(int, input().strip().split()))
        if len(query) == 2:
            func_dict.get(query[0], lambda x: None)(myQueue, query[1])
        else:
            func_dict.get(query[0], lambda x: None)(myQueue)
