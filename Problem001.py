#Problem 1 for Project Euler
#The goal is to find the sum of all multiples of 3, and 5 below 1000.

#from project Euler 9/4/2015
def PE1(a, b, n):
    '''Returns the sum of all multiples of a and b, below the positive integer n.'''
    def f(x, n):
        fl = int((n-1)/x)
        return x * fl * (fl+1)
    return (f(a,n) + f(b,n) - f(a*b,n))//2

print(PE1(3,5,1000))

#This is my favorite python solution for problem 1. There are no loops, because this solution requires no loops.

#I also enjoy the functions within functions.


#What we see in f, is our desired multiple being multiplied by the sum of the natural numbers 
#that index the number of those multiples below our limit.

#3+6+9+...+999 = 3(1+2+3+...+333)
#5+10+15+...+995 = 5(1+2+3+...+199)

#Then we simply add the union of the sets, and subtract their intersection resulting in the sum of two sets.
