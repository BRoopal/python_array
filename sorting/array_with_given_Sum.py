"""
input :      1   4   20   3   10   5
INDEX :      0   1   2    3   4    5
OUTPUT :     2    4
sum = 33,    l = 0,    r = 0,    curr_sum =0 """

def array_with_given_sum(arr, sum):

    l = 0
    r = 0
    curr_sum = 0
    for i in range(7):
        if (curr_sum < sum):
            print("right index:",r)
            curr_sum = curr_sum + arr[r]
            r += 1
            print("curr_sum:",curr_sum)

        elif (curr_sum > sum and curr_sum != sum):
            print("left index:", l)
            curr_sum = curr_sum - arr[l]
            l += 1
            print("curr_sum", curr_sum)


    print("left index:", l)
    print("right  index:", r-1)



arr = [1, 4, 20, 3, 10, 5]
n = len(arr)
sum = 33
array_with_given_sum(arr, sum)