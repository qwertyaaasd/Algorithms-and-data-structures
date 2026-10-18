n = int(input())
convs = []
for _ in range(n):
    convs.append(list(map(float, input().split())))

for conv in convs:
    stack = []
    conv = conv[1:]

    mins = [0] * len(conv)
    mins[-1] = conv[-1]
    for i in range(len(conv) - 2, -1, -1):
        mins[i] = conv[i] if conv[i] < mins[i + 1] else mins[i + 1]

    mn = mins[0]
    for i in range(len(conv)):
        if conv[i] > mn:
            stack.append(conv[i])
        elif conv[i+1:] and conv[i] == mn:
            mn = mins[i + 1]
            while stack and stack[-1] < mn:
                stack.pop()

    flag = True
    for i in range(len(stack) - 1):
        if stack[i] >= stack[i + 1]:
            continue
        else:
            flag = False
            break

    print(int(flag))