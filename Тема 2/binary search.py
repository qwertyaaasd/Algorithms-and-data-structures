def binary_search(arr, num):
    r = len(arr) - 1
    l = 0
    while l <= r:
        m = (l + r) // 2
        if arr[m] != num:
            if num > arr[m]:
                l = m + 1
            else:
                r = m - 1
        else:
            return True
        
    return False


n, k = map(int, input().split())
arr_n = list(map(int, input().split()))
arr_k = list(map(int, input().split()))

for el in arr_k:
    if binary_search(arr_n, el):
        print('YES')
    else:
        print('NO')
