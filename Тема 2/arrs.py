def binary_search(arr, x):
    l = 0
    r = len(arr) - 1
    left = -1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == x:
            left = m
            r = m - 1
        elif arr[m] > x:
            r = m - 1
        else:
            l = m + 1

    if left == -1:
        return 0

    l = 0
    r = len(arr) - 1
    right = -1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == x:
            right = m
            l = m + 1
        elif arr[m] > x:
            r = m - 1
        else:
            l = m + 1

    return right - left + 1 


n = int(input())
arr1 = sorted(list(map(int, input().split())))
m = int(input())
arr2 = list(map(int, input().split()))

for el in arr2:
    print(binary_search(arr1, el), end=' ')
