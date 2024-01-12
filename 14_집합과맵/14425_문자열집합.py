import sys
n, m = map(int, sys.stdin.readline().split()) 

str1 = set()
str2 = []

for _ in range(n):
    str1.add(sys.stdin.readline().rstrip())
    
for _ in range(m):
    str2.append(sys.stdin.readline().rstrip())
    
cnt = 0

for i in range(m):
    if str2[i] in str1:
        cnt += 1
    
print(cnt)