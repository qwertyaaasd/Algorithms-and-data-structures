lst = list(map(int, input().split()))
n = lst[0]
lst = lst[1:]

stack = []

total = 0
for el in lst:
    if stack and el != stack[-1][0] and stack[-1][1] >= 3:
        color, cnt = stack.pop()
        total += cnt
        # if stack and stack[-1][0] == color:
        #     stack[-1][1] += cnt

    if stack and stack[-1][0] == el:
        stack[-1][1] += 1
    else:
        stack.append([el, 1])

if stack and stack[-1][1] >= 3:
    color, cnt = stack.pop()
    total += cnt

print(total)