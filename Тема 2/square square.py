def f(x):
    return x**2 + x**(1/2)


c = float(input())
exp = 1e-10
l = 0
r = c
for i in range(100):
    x = (l + r) / 2
    if abs(f(x) - c) > exp:
        if f(x) > c:
            r = x
        else:
            l = x
            
x = (l + r) / 2
print(f'{x:.10f}')
