def sieve(n):
    arr = [False, False] + [True for i in range(2, 2*n+1)]
    for i in range(2, 2*n+1):
        if arr[i]:
            for j in range(i+i, 2*n+1, i):
                arr[j] = False
    prime = [i for i in range(n+1, 2*n+1) if arr[i] == True]
    return len(prime)


while True:
    n = int(input())
    if n == 0: break
    print(sieve(n))