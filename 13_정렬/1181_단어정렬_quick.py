n = int(input())

ls = []

for i in range(n):
    ls.append(input())
    
def dictcheck(x, y):
    for i in range(len(x)):
        if ord(x[i]) == ord(y[i]):
            continue
        elif ord(x[i]) < ord(y[i]):
            return True
        else:
            return False

def quick(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    rest = arr[1:]
    left = [x for x in rest if len(x) < len(pivot) or (len(x)==len(pivot) and dictcheck(x, pivot))]
    right = [x for x in rest if len(x) > len(pivot) or (len(x)==len(pivot) and not dictcheck(x, pivot))]
    
    return quick(left) + [pivot] + quick(right)

for item in quick(list(set(ls))):
    print(item)