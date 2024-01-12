import sys
import math
n = int(sys.stdin.readline().rstrip())

def isPrime(num):
    for i in range(2, math.floor(math.sqrt(num))+1):
        if num%i == 0:
            return False
    return True

for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    while not isPrime(a) or a == 0 or a == 1:
        a += 1
    print(a)