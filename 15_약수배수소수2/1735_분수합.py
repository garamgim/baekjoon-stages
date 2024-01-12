a, b = map(int, input().split())
c, d = map(int, input().split())
n, m = a*d+b*c, b*d

def gcd(a, b):
    if b > a:
        a, b = b, a
    while a % b != 0:
        a = a%b
        a, b = b, a
    return b


while (gcd(n,m) != 1):
    cd = gcd(n,m)
    n /= cd
    m /= cd

print(int(n),int(m))