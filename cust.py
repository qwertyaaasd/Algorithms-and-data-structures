import heapq as h

n = int(input())

goods = []
for _ in range(n):
    good = list(map(int, input().split()))
    goods.append(tuple([good[0], sum(good)]))

h.heapify(goods)

apparatus = []
while goods != []:
    good = h.heappop(goods)
    if apparatus and apparatus[0] <= good[0]:
        h.heappop(apparatus)

    h.heappush(apparatus, good[1])

print(len(apparatus))