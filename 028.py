"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10

19  6  1  2 11

18  5  4  3 12

17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?


"""

"""pattern 
   diagonal nums
2     3   5  7  9
4     13 17 21 25
6     31 37 43 49
8     57 65 73 81
.
.
1000
"""      

def ps(n=1001):
    totalsum = 0
    start = 1
    for j in range(2, n, 2):
        alist = [start+j*i for i in range(1, 5)]
        start = alist[-1]
        totalsum += sum(alist)
    return totalsum + 1   
