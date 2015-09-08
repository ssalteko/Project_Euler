#Problem 10 from proect Euler
#The goal is to sum all primes below 2M.
#I got this short beutiful code from the forum authored by lassevk 9/7/2015
    
def sumprimes(n):
    '''this sums primes below the value n'''
    m = [0] * n
    j = 3
    sumofprimes = 2
    while j < n:
        if m[j] == 0:
            sumofprimes += j
            p = j
            while p < n:
                m[p] = 1
                p += j
        j += 2
    print (sumofprimes)
