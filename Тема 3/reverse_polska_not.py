s = input().split()

stack = []
for el in s:
    if not el.isnumeric():
        b = stack.pop()
        a = stack.pop()
        if el == '+':
            stack.append(a+b)
        elif el == '-':
            stack.append(a-b)
        elif el == '*':
            stack.append(a*b)
        elif el == '/':
            stack.append(a/b)
        
    else:
        stack.append(int(el))

print(stack[0])