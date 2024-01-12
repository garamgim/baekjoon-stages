import sys

class Queue():
    def __init__(self):
        self.queue = []
    
    def push(self, n):
        if len(self.queue) == 0:
            self.queue.append(n)
        else:
            self.queue.insert(0, n)
    
    def pop(self):
        if len(self.queue) != 0:
            a = self.queue.pop()
            return a
        else:
            return -1
    
    def size(self):
        return len(self.queue)

    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0
    
    def front(self):
        return self.queue[-1] if len(self.queue) != 0 else -1
    
    def back(self):
        return self.queue[0] if len(self.queue) != 0 else -1
    
    def get(self):
        return self.queue
        
n = int(sys.stdin.readline().rstrip())
q = Queue()

for i in range(n):  
    op = sys.stdin.readline().rstrip()
    if op == "pop":
        print(q.pop())
    elif op == "size":
        print(q.size())
    elif op == "empty":
        print(q.empty())
    elif op == "front":
        print(q.front())
    elif op == "back":
        print(q.back())
    else:
        p, n = op.split()
        n = int(n)
        q.push(n)
    