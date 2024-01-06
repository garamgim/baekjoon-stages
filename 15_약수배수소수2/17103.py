import sys
n = int(sys.stdin.readline().rstrip())


arr = [False, False] + [True]*999999
for i in range(2, 1000001):
    if arr[i]:
        for j in range(i+i, 1000001, i):
            arr[j] = False

for i in range(n):
    num = int(sys.stdin.readline().rstrip())
    cnt = 0
    for j in range(2, num//2+1):
        if arr[j] and arr[num-j]:
            cnt += 1
    print(cnt)
