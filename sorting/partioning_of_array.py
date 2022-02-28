def partioning (arr, pivot):
    # i to end :-  unknown
    # 0 to j-1 :-  >= pivot
    # j to i-1 :-  >pivot
    i, j = 0, 0
    while (i < len(arr)):
        if (arr[i] > pivot):
            i += 1
        else:
            arr[i] , arr[j] = arr[j], arr[i]
            i += 1
            j += 1


#input take from user
#print("enter the element of array : ")
#arr = [int(i) for i in input().split()]
#static input:
arr = [7, 9, 4, 8, 3, 6, 2, 1]
print(" enter the value of pivot :")
#pivot = int(input())
pivot = int(5)
#print(arr , pivot)
partioning (arr, pivot)
print (arr)
# output : [4, 3, 2, 1, 9, 6, 7, 8]