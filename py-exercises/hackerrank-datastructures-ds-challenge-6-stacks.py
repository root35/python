# Enter your code here. Read input from STDIN. Print output to STDOUT

func_dict = {
    1: lambda stack, item: stack.push(item),
    2: lambda stack: stack.pop(),
    3: lambda stack: stack.find_max(),
}


class Stack:
    def __init__(self):
        self.stack = []
        self.max_values = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, obj):
        self.stack.append(obj)
        if len(self.max_values) == 0:
            self.max_values.append(obj)
        elif obj > self.max_values[-1]:
            self.max_values.append(obj)

    def pop(self):
        if self.isEmpty():
            return None

        popped = self.stack.pop()
        if popped == self.max_values[-1] \
          and not popped in self.stack:
            self.max_values.pop()
        return popped

    def peek(self):
        if self.isEmpty():
            return None
        return self.stack[-1]

    def find_max(self):
        if self.isEmpty():
            print('')
        print(self.max_values[-1])


if __name__ == '__main__':
    n_queries = int(input())
    myStack = Stack()

    for _ in range(n_queries):
        tmp_query = input().rstrip().split()
        query = [int(q) for q in tmp_query]
        if len(query) == 2:
            func_dict.get(query[0], lambda: None)(myStack, query[1])
        else:
            func_dict.get(query[0], lambda: None)(myStack)
