import math

n = int(input())

trees = []

for i in range(n):
    trees.append(int(input()))
    
space = []

for i in range(1, len(trees)):
    space.append(trees[i] - trees[i-1])

g = space[0]
cnt = 0

for i in range(1, len(space)):
    g = math.gcd(g, space[i])

for i in range(len(space)):
    cnt += space[i]/g - 1
    
print(int(cnt))