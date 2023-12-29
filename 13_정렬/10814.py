import sys
n = int(sys.stdin.readline())

ls = []

for i in range(n):
    a, b = sys.stdin.readline().strip().split()
    ls.append([int(a), b])
    
ls.sort(key = lambda x:x[0])
    
for item in ls:
    print(*item)