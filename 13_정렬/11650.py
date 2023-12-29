n = int(input())
ls = []

for i in range(n):
    a, b = map(int, input().split())
    ls.append((a, b))

ls.sort()

for item in ls:
    print(*item)