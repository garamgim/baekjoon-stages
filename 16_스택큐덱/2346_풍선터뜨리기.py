import sys

n = int(sys.stdin.readline().rstrip())

balloons = list(enumerate(map(int, sys.stdin.readline().rstrip().split()), start = 1))
idx = 0

while balloons:
    popped = balloons.pop(idx)
    print(popped[0], end = ' ')
    if popped[1] > 0 and balloons:
        idx += (popped[1] - 1)
        idx = idx % len(balloons)
    elif popped[1] < 0 and balloons:
        idx += popped[1]
        idx = idx % len(balloons)