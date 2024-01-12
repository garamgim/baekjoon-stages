n = int(input())
s = set(map(int, input().split()))
m = int(input())
crd = list(map(int, input().split()))
ans = []
for i in range(len(crd)):
    if crd[i] in s:
        ans.append(1)
    else:
        ans.append(0)
print(*ans)