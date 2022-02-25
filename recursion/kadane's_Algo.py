def maxsubarraysum(arr, n):
    max_so_far = arr[0]
    curr_max = arr[0]
    left = 0
    right = 0
    for i in range(1, n):
        curr_max = max(arr[i], curr_max + arr[i])

        if (curr_max == arr[i]):
            left = i

        if (curr_max >= max_so_far):
            right = i

        max_so_far = max(max_so_far, curr_max)

    print("left index:", left)
    print("right index:", right)

    print("max sum element:")
    for i in range(left, right + 1):
        print(arr[i], end=" ")

    return max_so_far

#input take from user
print("enter the element of array : ")
arr = [int(i) for i in input().split()]
#static input:
#arr = [-2, -3, 4, -1, -2, 1, 5, 2, -3]
n = len(arr)
print("\nmax contigous sum is : ", maxsubarraysum(arr, n))
