import sys
scanner = sys.stdin.readline

n = int(scanner())

mycard = list(map(int, scanner().split()))
dict = {}

for num in mycard:
    if num in dict:
        dict[num] += 1
    else:
        dict[num] = 1

m = int(scanner())

card = list(map(int, scanner().split()))
for num in card:
    if num in dict:
        print(dict[num], end=" ")
    else:
        print(0, end=" ")