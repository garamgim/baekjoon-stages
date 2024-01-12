import sys
from collections import deque
        
n = int(sys.stdin.readline().rstrip())
q = deque()

for i in range(n):  
    op = sys.stdin.readline().rstrip()
    if op == "pop":
        print(q.popleft()) if len(q) != 0 else print(-1)
    elif op == "size":
        print(len(q))
    elif op == "empty":
        print(1) if len(q) == 0 else print(0)
    elif op == "front":
        print(q[0]) if len(q) != 0 else print(-1)
    elif op == "back":
        print(q[-1]) if len(q) != 0 else print(-1)
    else:
        p, n = op.split()
        n = int(n)
        q.append(n)
    