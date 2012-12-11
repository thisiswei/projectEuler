#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
#we can see that the 6th prime is 13.
#What is the 10001st prime number?




def isprime(n):
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

def ps7(n):
    pos = 1
    x = 3
    while pos < n: 
        if isprime(x):
            pos += 1
        x += 2
    print x - 2

        
