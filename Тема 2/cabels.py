def good(arr, k, m):
    cnt = 0
    for i in range(len(arr)):
        cnt += arr[i] // m

    return cnt >= k


n, k = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(int(input()))

l = 0
r = 10000001
while r - l > 1:
    m = (l + r) // 2
    if good(arr, k, m):
        l = m
    else:
        r = m

print(l)
