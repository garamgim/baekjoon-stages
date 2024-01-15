class Josephus():
    def __init__(self, n):
        self.items = [i for i in range(1, n+1)]

    def __len__(self):
        return len(self.items)
    
    def kill(self, idx):
        return self.items.pop(idx)
    
n, k = map(int, input().split())
table = Josephus(n)
ans = []

idx = k-1

ans.append(table.kill(idx))

for i in range(n-1):
    idx += k-1
    if idx >= len(table):
        idx = idx % len(table)
        ans.append(table.kill(idx))
    else: 
        ans.append(table.kill(idx))

ans_str = ", ".join(map(str, ans))
print(f"<{ans_str}>")