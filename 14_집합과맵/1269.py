import sys
scanner = sys.stdin.readline

n, m = map(int, scanner().split())

a = set(map(int, scanner().split()))
b = set(map(int, scanner().split()))
    
print(len(a-b)+len(b-a))