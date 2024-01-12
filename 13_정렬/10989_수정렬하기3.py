import sys
n = int(sys.stdin.readline())

dct = {}

for i in range(n):
    a = int(sys.stdin.readline().strip())
    if a in dct:
        dct[a] += 1
    else:
        dct[a] = 1
        
ans = sorted(dct.items())

for item in ans:
    for i in range(item[1]):
        print(item[0])