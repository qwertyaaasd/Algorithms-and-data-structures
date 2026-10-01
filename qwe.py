def good(n, a, b, w, h, d):
    if (w//(a + 2*d))*(h//(b + 2*d)) >= n:
        return True
    if (w//(b + 2*d))*(h//(a + 2*d)) >= n:
        return True
    return False


n, a, b, w, h = map(int, input().split())
l = 0
r = 10**18
while r - l > 1:
    m = (l + r) // 2
    if good(n, a, b, w, h, m):
        l = m
    else:
        r = m

print(l)