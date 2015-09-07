# Problem 006 from Project Euler

def sumsquares(n):
    b = (n*(n+1)*(2*n+1))//6
    return b

def squaresum(n):
    b = ((n*(n+1))//2)
    return b

print(squaresum(100)**2 - sumsquares(100))


