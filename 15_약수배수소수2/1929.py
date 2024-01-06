import sys
import math
n, m = map(int, sys.stdin.readline().split())

def isPrime(num):
    for i in range(2, math.floor(math.sqrt(num))+1):
        if num%i == 0:
            return False
    return True

for i in range(n, m+1):
    if i == 1:
        continue
    if isPrime(i):
        print(i)
