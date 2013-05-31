"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.  
Find the largest palindrome made from the product of two 3-digit numbers.
"""


def ps4():
    for i in range(999*999, 100*100, -1):
        if str(i) == str(i)[::-1]:
            for j in range(999, 100, -1):
                if not i % j:
                    if len(str(i/j)) == 3:
                        return i, j


