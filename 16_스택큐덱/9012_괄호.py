import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    stk = []
    p = list(sys.stdin.readline().rstrip())
    for i in range(len(p)):
        if p[i] == '(':
            stk.append(p[i])
        else:
            if len(stk) > 0 and stk[-1] == '(':
                stk.pop()
            else:
                stk.append(')')
    if len(stk) > 0:
        print("NO")
    else:
        print("YES")