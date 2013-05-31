"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.  
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""
def ps5():
    for i in range(2520, 100000000000, 2520):
        if all(i % j == 0 for j in range(1, 21)):
            return i
