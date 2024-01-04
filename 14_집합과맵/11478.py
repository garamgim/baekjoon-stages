str = input()
ans = set()

for i in range(len(str)-1, -1, -1):
    for j in range(len(str)):
        ans.add(str[j:j+i])
        
print(len(ans))