from random import randint

def quick_sort(arr, left, right):
    if left < right:
        mid = arr[randint(left, right)]
        i, j = left, right
        while i <= j:
            while arr[i] < mid:
                i += 1
            while arr[j] > mid:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j-= 1

        quick_sort(arr, left, j)
        quick_sort(arr, i, right)

        return arr
    else:
        return arr

n = int(input())
arr = list(map(int, input().split()))

print(* quick_sort(arr, 0, n-1))