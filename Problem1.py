#Problem 1 for Project Euler

#This is my favorite python solution. There are no loops, because this solution requires no loops.

#from project Euler 9/4/2015
def PE1(a, b, n):
    def f(x, n):
        fl = int((n-1)/x)
        return x * fl * (fl+1)
    return (f(a,n) + f(b,n) - f(a*b,n))//2
