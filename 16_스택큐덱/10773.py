import sys
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop() if len(self.items) > 0 else -1
    
    def sum(self):
        s = 0
        for i in range(len(self.items)):
            s += self.items[i]
        return s
    

n = int(sys.stdin.readline().rstrip())

stack = Stack()

for i in range(n):
    n = int(input())

    if n > 0:
        stack.push(n)
    else:
        stack.pop()

print(stack.sum())