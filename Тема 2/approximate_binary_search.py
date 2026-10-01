def approximate_bs(arr, num):
    l = -1
    r = len(arr)
    a, b = arr[0], arr[0]
    while r - l > 1:
        m = (l + r) // 2
        if arr[m] == num:
            return arr[m]
        elif arr[m] < num:
            if r == len(arr):
                a, b = arr[m], arr[m]
            else:
                a, b = arr[m], arr[m+1]
            l = m
        else:
            if l == -1:
                a, b = arr[m], arr[m]
            else:
                a, b = arr[m-1], arr[m]
            r = m
            
    if abs(a - num) > abs(b - num):
        return b
    elif abs(a - num) == abs(b - num):
        return min(a, b)
    else:
        return a


n, k = map(int, input().split())
arr_n = list(map(int, input().split()))
arr_k = list(map(int, input().split()))

for el in arr_k:
    print(approximate_bs(arr_n, el))
