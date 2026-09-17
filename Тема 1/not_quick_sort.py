from random import *

def not_quick_sort(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 2]
    else:
        arr = list(range(1, n+1))

        arr[1], arr[2] = arr[2], arr[1]
        for i in range(3, n):
            mid = i // 2
            arr[mid], arr[i] = arr[i], arr[mid]
        
        return arr


n = int(input())
arr = not_quick_sort(n)
print(* arr)