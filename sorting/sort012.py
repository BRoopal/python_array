"""         i                 k
input:      1 2 1 2 0 0 2 1 2 1
            j
                  i         k
            1 1 1 2 0 0 2 1 2 2
            j
                  i       k
            1 1 1 2 0 0 2 1 2 2
            j

                   i    k
            1 1 1 1 0 0 2 2 2 2
            j

                    i  k
            1 1 1 1 0 0 2 2 2 2
            j

                    i  k
            1 1 1 1 0 0 2 2 2 2
            j

                      i,k
            0 1 1 1 1 0 2 2 2 2
              j

                      k i
            0 0 1 1 1 1 2 2 2 2
                j



            arr[i] == 0                               arr[i] == 1              arr[i] == 2
            arr[i], arr[j] = arr[j], arr[i]                i++             arr[i], arr[k] = arr[k], arr[i]
            i++                                                                  k--
            j++









                j     k i
output:     0 0 1 1 1 1 2 2 2 2

 to end : unknown
0 to j-1 : 0
j to i-1 : 1
k+1 to e : 2

"""
def sort123 (arr):
    i, j = 0, 0
    k = len(arr)-1
    while(i <= k):
        if (arr[i] == 0):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1

        elif (arr[i] == 1):
            i += 1

        elif (arr[i] == 2):
            arr[i], arr[k] = arr[k], arr[i]
            k -= 1

arr = [1, 2, 1, 2, 0, 0, 2, 1, 2, 1]
sort123 (arr)
print("sorted element: ",arr)