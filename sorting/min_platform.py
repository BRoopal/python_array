# t1     t2    t3    t4      t5    t6
"""Input: arv[] = {9:00, 9:40, 9:50, 11:00, 15:00, 18:00} 
          dep[] = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00} 
          dep[] = {9:10, 11:20, 11:30, 12:00, 19:00, 20:00}
          
Output: 3 
Explanation: There are at-most three trains at a time (time between 9:40 to 12:00)"""


def min_platform(arv, dep, n):
    needed_platform = 1
    minimum_platform = 1
    i = 1
    j = 0
    while (i < n and j < n ):
        if (arv[i] > dep[j]):
            needed_platform -= 1
            j += 1
        elif (arv[i] < dep[j]):
           needed_platform += 1
           i += 1

    if (needed_platform > minimum_platform):
            minimum_platform = needed_platform
    return minimum_platform

arv = [900, 940, 950, 1100, 1500, 1800]
n = len(arv)
# dep timing is sorted
dep = [910, 1120, 1130, 1200, 1900, 2000]
a = min_platform(arv, dep, n)
print("minimum platform:",a)

