import sys
input = sys.stdin.readline

n = int(input())
staffs = {}

for _ in range(n):
    name, status = input().split()
    staffs[name] = status

staffs_in = []

for name in staffs:
    if staffs[name] == 'enter':
        staffs_in.append(name)

staffs_in.sort(reverse = True)

for name in staffs_in:
    print(name)