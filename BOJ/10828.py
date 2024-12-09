class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1
        self.len = 0
    
    def push(self, item):
        self.stack.append(item)
        self.top += 1
        self.len += 1
        return True
    
    def pop(self):
        if self.top == -1:
            return -1
        ans = self.stack.pop()
        self.top -= 1
        self.len -= 1
        return ans
    
    def length(self):
        return self.len
    
    def empty(self):
        if self.top == -1:
            return 1
        return 0
    
    def get_top(self):
        if self.top == -1:
            return -1
        return self.stack[self.top]

n = int(input())

stack = Stack()

commands = []
for _ in range(n):
    bunch = tuple(input().split())
    commands.append(bunch)

for c in commands:
    if len(c) == 1:
        command = c[0]
    else:
        command, item = c[0], c[1]
    
    if command == 'push':
        stack.push(int(item))
    elif command == 'pop':
        print(stack.pop())
    elif command == 'size':
        print(stack.length())
    elif command == 'empty':
        print(stack.empty())
    else:
        print(stack.get_top())
