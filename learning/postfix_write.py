stack = []
for elem in input().split():

    if elem in '+-*/':
        b = int(stack.pop())
        a = int(stack.pop())
        if elem == '+':
            res = a + b
            stack.append(res)
        elif elem == '-':
            res = a - b
            stack.append(res)
        elif elem == '*':
            res = a * b
            stack.append(res)
        elif elem == '/':
            res = a / b
            stack.append(res)
    else:
        stack.append(elem)

print(*stack)