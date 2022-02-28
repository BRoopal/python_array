def partition(arr, pivot, lo, hi):
    print("pivot ->", +pivot)
    i, j = lo, lo
    while (i <= hi):
        if (arr[i] <= pivot):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        else:
            i += 1
    print("pivot index ->", +(j - 1))
    return (j - 1)

def quicksort(arr, lo, hi):
    if (lo >= hi):
        return
    print(arr)
    pivot = arr[hi]
    pi = partition(arr, pivot, lo, hi)
    quicksort(arr, lo, pi - 1)
    quicksort(arr, pi + 1, hi)

arr = [8, 5, 1, 3, 7, 2, 9, 6]
n = len(arr)
lo = 0
hi = n - 1
print(" -> ", quicksort(arr, lo, hi))
print("sorted arr:", arr)

"""
[8, 5, 1, 3, 7, 2, 9, 6]
pivot -> 6
pivot index -> 4
[5, 1, 3, 2, 6, 8, 9, 7]
pivot -> 2
pivot index -> 1
[1, 2, 3, 5, 6, 8, 9, 7]
pivot -> 5
pivot index -> 3
[1, 2, 3, 5, 6, 8, 9, 7]
pivot -> 7
pivot index -> 5
[1, 2, 3, 5, 6, 7, 9, 8]
pivot -> 8
pivot index -> 6
 ->  None
sorted arr: [1, 2, 3, 5, 6, 7, 8, 9]

"""
