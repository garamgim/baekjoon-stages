n = int(input())
ls = []

for i in range(n):
    a, b = map(int, input().split())
    ls.append((b, a))

ls.sort()

for item in ls:
    print(item[-1], item[0])