## Problem 9 form Project Euler
##Authored by Steve Saltekoff on Fri 21 2015


def pythtriptester(a,b,c,n):
    if a+b+c == n:
        return 1,a,b,c
    else:
        return 0,a,b,c

def pythtrip(j,k,n):
    a = j**2 + k**2
    b = 2*j*k
    c = j**2 - k**2
    z = pythtriptester(a,b,c,n)
    return(z)


def PythagTripPerim(n):
    j = 2
    k = 1
    while j+k <= 2*j  :
        z = pythtrip(j,k,n)
        if k!=j:
            k += 1
        else:
            j += 1
            k = 1
        if z[0] == 1 and z[3] != 0:
            return z[1],z[2],z[3]
        if z[1]>n:
            return 0
