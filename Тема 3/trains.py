n = int(input())
train = list(map(int, input().split()))

stack = []
cnt = 1

for wagon in train:
    if wagon == cnt:
        cnt += 1
    else:
        stack.append(wagon)

    while stack != [] and stack[-1] == cnt:
        stack.pop()
        cnt += 1

if stack == [] and cnt == n + 1:
    print('YES')
else:
    print('NO')