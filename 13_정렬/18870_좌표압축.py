import sys
n = int(sys.stdin.readline())

ls = list((map(int, sys.stdin.readline().split())))

srt = sorted(list(set(ls)))
dct = {}

for i in range(len(srt)):
    dct[srt[i]] = i

for num in ls:
    print(dct[num], end=" ")