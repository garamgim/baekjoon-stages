import sys


while True:
    input = sys.stdin.readline().rstrip()
    stk = []

    if input == '.':
        break

    for i in range(len(input)):
        if input[i] == '(' or input[i] == '[':
            stk.append(input[i])
        elif input[i] == ')':
            if len(stk) > 0 and stk[-1] == '(':
                stk.pop()
            else:
                stk.append(input[i])
        elif input[i] == ']':
            if len(stk) > 0 and stk[-1] == '[':
                stk.pop()
            else:
                stk.append(input[i])

    if len(stk) > 0:
        print("no")
    else:
        print("yes")

 


