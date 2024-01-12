import sys

n = int(input())
ans = []

for i in range(n):
    ans.append(int(sys.stdin.readline()))
    
for num in sorted(ans):
    print(num)