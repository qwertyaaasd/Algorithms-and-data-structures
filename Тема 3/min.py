from collections import deque

n, k = map(int, input().split())
lst = list(map(int, input().split()))

dq = deque()
for i in range(n):
    if dq != deque() and dq[0] < i - k + 1:
        dq.popleft()

    while dq != deque() and lst[dq[-1]] >= lst[i]:
        dq.pop()

    dq.append(i)

    if i >= k - 1:
        print(lst[dq[0]])