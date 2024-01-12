import sys
scanner = sys.stdin.readline

n, m = map(int, scanner().split())
nohear = set()
nosee = set()

for _ in range(n):
    nohear.add(scanner().rstrip())

for _ in range(m):
    nosee.add(scanner().rstrip())
    
nohear_nosee = sorted(list(nohear & nosee))

print(len(nohear_nosee))
for name in nohear_nosee:
    print(name)