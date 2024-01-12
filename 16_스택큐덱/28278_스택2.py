import sys
class Stack:
    def __init__(self):
        self.items = []
    
    def __len__(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop() if len(self.items) > 0 else -1
    
    def isEmpty(self):
        return 0 if len(self.items) > 0 else 1

    def hasNum(self):
        return self.items[-1] if len(self.items) > 0 else -1
    

n = int(sys.stdin.readline().rstrip())

stack = Stack()

for i in range(n):
    order = sys.stdin.readline().rstrip()

    if order == "2":
        a = stack.pop()
        print(a)
    elif order == "3":
        print(len(stack))
    elif order == "4":
        print(stack.isEmpty())
    elif order == "5":
        print(stack.hasNum())
    else:
        a, b = map(int, order.split())
        stack.push(b)
