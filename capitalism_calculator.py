import heapq as h

n = int(input())
ls = list(map(int, input().split()))

P = 0.05

h.heapify(ls)

total = 0
while len(ls) > 1:
    sm = 0
    for _ in range(2):
        sm += h.heappop(ls)

    total += sm * P
    h.heappush(ls, sm)

print(f'{total:.2f}')