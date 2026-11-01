import heapq as h

n = int(input())
aquas = []
for i in range(n):
    a = int(input())
    h.heappush(aquas, (max(1000 - a, 1), i, a))

prev = 0
total = 0
while aquas:
    t, i, a = h.heappop(aquas)

    if abs(prev - i) > abs(t - total):
        print(t)
        break

    total = t
    prev = i
    a += 1
    new_t = t + max(1000 - a, 1)

    h.heappush(aquas, (new_t, i, a))