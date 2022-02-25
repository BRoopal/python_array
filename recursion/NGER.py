#input :     5 8 1 3 9   4  5  2
#output:     8 9 3 9 -1  5 -1 -1
""" pop answer pull
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