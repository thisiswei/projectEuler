"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.  
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""
billion = 1000000000

def ps5():
    j = 2520 
    for j in range(j,1*billion,j):
        if not any([j % i for i in range(1,21)]): 
            return j  
