def f(a, b, c, d, x):
    return a*x**3 + b*x**2 + c*x + d


a, b, c, d = map(int, input().split())
exp = 1e-15
l = -1e9
r = 1e9

for i in range(100):
    m = (l + r) / 2
    if abs(f(a, b, c, d, m)) > exp:
        if f(a, b, c, d, m) * f(a, b, c, d, r) > 0:
            r = m
        else:
            l = m

m = (l + r) / 2
print(f'{m:.15f}')