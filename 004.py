"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.  
Find the largest palindrome made from the product of two 3-digit numbers.
"""


maximum = 999*999
minimum = 100*100 

def is_p(n):
    digits = str(n) 
    return digits[::-1] == digits

def find():
    for i in range(maximum,minimum,-1):
        if is_p(i): 
            for j in range(999,100,-1):
                if not i % j:
                    if len(str(i/j)) == 3:
                        return i,j   


