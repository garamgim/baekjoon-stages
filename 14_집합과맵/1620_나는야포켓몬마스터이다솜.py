import sys

n, m = map(int, sys.stdin.readline().split())
pokemon = {}

for i in range(n):
    name = sys.stdin.readline().rstrip()
    pokemon[str(i+1)] = name
    pokemon[name] = str(i+1)

for _ in range(m):
    q = sys.stdin.readline().rstrip()
    print(pokemon[q])
