def ngerORTL(arr,n):
    stack = []
    print(arr[n - 1], -1)
    stack.append(arr[n-1])

    #print(stack)
    for i in range (len(arr)-2, -1, -1):


        #print (arr[i])

        while ((len(stack) > 0)):
            if(stack[len(stack) - 1] > arr[i]):
                print(arr[i],stack[len(stack) - 1])
                break
            else:
                stack.pop()

        if(len(stack) == 0):
            print(arr[i], -1)
        stack.append(arr[i])

#print(stack.pop(), -1)
arr = [5, 8, 1, 3, 9, 4, 5, 2]
n = len(arr)
ngerORTL(arr,n)
"""2, -1
5, -1
4,  5
9, -1
3,  9
1,  3
8,  9
5,  8

LOGIC:

#input :     5 8 1 3 9   4  5  2
#output:     8 9 3 9 -1  5 -1 -1
 pop answer pull
r to l:
stack     curr      pop         ans        push
2                                -1
2           5        2           -1        5
5           4                     5        4
5,4         9        4,5         -1        9
9           3                     9        3
9,3         1                     3        1
9,3,1       8        1,3          9        8
9,8         5                     8        5
9,8,5
"""
