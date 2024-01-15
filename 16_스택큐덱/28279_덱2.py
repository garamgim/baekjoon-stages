import sys
from collections import deque
n = int(sys.stdin.readline())

dq = deque()

for i in range(n):
    order = sys.stdin.readline().rstrip()
    if order == "3":
        print(dq.popleft()) if len(dq) != 0 else print(-1)
    elif order == "4": 
        print(dq.pop()) if len(dq) != 0 else print(-1)
    elif order == "5":
        print(len(dq))
    elif order == "6":
        print(1) if len(dq) == 0 else print(0)
    elif order == "7":
        print(dq[0]) if len(dq) != 0 else print(-1)
    elif order == "8":
        print(dq[-1]) if len(dq) != 0 else print(-1)
    else:
        od, num = order.split()
        if od == "1":
            dq.appendleft(int(num))
        else:
            dq.append(int(num))