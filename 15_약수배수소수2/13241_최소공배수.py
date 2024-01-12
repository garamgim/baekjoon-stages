import sys

a, b = map(int, sys.stdin.readline().split())
mul = a*b
if b > a:
    a, b = b, a
while a % b != 0:
    remain = a%b
    a = b
    b = remain
gcd = b
print(int(mul/gcd))