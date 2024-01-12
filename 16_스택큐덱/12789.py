n = int(input())

old = list(map(int, input().split()))
everyone = len(old)
done = []
stk = []

while len(done) != everyone:
    if len(done) == 0 and old[0] == 1:
        a = old.pop(0)
        done.append(a)
    elif len(done) > 0 and len(old) > 0 and done[-1]+1 == old[0]:
        a = old.pop(0)
        done.append(a)
    elif len(done) > 0 and len(stk) > 0 and done[-1]+1 == stk[-1]:
        a = stk.pop()
        done.append(a)
    elif len(old) > 0:
        a = old.pop(0)
        stk.append(a)
    else:
        break


if len(stk) > 0:
    print("Sad")
else:
    print("Nice")    




