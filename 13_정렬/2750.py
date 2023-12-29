n = int(input())
ls = []

for i in range(n):
    ls.append(int(input()))
    
for i in range(1, len(ls)):
    for j in range(i-1, -1, -1):
        if ls[j] > ls[j+1]:
            ls[j], ls[j+1] = ls[j+1], ls[j]
        else:
            break

for num in ls:
    print(num)
