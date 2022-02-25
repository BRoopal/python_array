def ngerBF(arr, n):
    a = -1
    for i in range(n - 1):
        # print(arr[i])

        for j in range(i + 1, n):
            if (arr[i] < arr[j]):
                print(arr[j], end=" ")
                break
            elif (j == n - 1):
                print(a)

    # last element always have -1
    print(a)

#input take from user
print("enter the element of array : ")
arr = [int(i) for i in input().split()]
#static input:
#arr = [11, 13, 21, 25, 12]
n = len(arr)
ngerBF(arr, n)
