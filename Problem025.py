#Problem 025 from Project Euler.
#The goal is to find the index of the first fibionocci number to have 1000 digits.
#Authored by Steve Saltekoff on 9/9/2015, and was used to submit my answer.

def intlength(n):
    '''returns the length of an integer.'''
    l = len(str(n))
    return l

def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a

i = 12
a = 0

while intlength(fib(i)) != 1000:
    a = fib(i)
    #print(i,fib(i))
    i = i+1
print(i)
