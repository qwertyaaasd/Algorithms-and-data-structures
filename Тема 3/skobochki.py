s = input()
stack = []

flag = True
for el in s:
    if el in '([{':
        stack.append(el)
        continue
    if len(stack) != 0 and (el == ')' and stack[-1] == '(' or 
                              el == ']' and stack[-1] == '[' or
                              el == '}' and stack[-1] == '{'):
        stack.pop()
    else:
        flag = False
        break

if len(stack) != 0:
    flag = False

print('yes' if flag else 'no')