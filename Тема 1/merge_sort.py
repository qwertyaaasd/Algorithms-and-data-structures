def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        i = j = 0
        res = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1

        res += left[i:] + right[j:]

        return res
    
    else:
        return arr


n = int(input())
arr = list(map(int, input().split()))

print(* merge_sort(arr))
