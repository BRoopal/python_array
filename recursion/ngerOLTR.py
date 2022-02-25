def ngerOLTR(arr, n):
    stack = []
    stack.append(arr[0])
    #top = stack[len(stack) - 1]
    for i in range(1, n):
        while ((len(stack) > 0) and stack[len(stack) - 1] < arr[i]):
            print(stack.pop(), arr[i])
        stack.append(arr[i])
    while ((len(stack) > 0)):
        print(stack.pop(), -1)

#input take from user
#print("enter the element of array : ")
#arr = [int(i) for i in input().split()]
#static input:
arr = [5, 8, 1, 3, 9, 4, 5, 2]
n = len(arr)
ngerOLTR(arr, n)

# LOGIC
# input :     5 8 1 3 9   4  5  2
# output:     8 9 3 9 -1  5 -1 -1
# l to r :
# stack     curr      pop         ans        push
# 5           5
#             8       5           8          8
# 8           1                              1
# 8,1         3       1           3          3
# 8 3         9       3,8         9,9          9
# 9           4                              4
# 9,4         5       4           5          5
# 9,5         2                              2
# remaining in stack
# 9,5,2                        -1,-1,-1

