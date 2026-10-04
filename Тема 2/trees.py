def good(a, k, b, m, x, mid):
    # print((a+b)*mid - (mid//k * a) - (mid//m * b))
    return ((a+b)*mid - (mid//k * a) - (mid//m * b)) >= x
        

a, k, b, m, x = map(int, input().split())

l = 0
r = x
while r - l > 1:
    mid = (r + l) // 2
    if good(a, k, b, m, x, mid):
        r = mid
    else:
        l = mid

print(r)