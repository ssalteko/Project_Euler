#Problem 3 from Project Euler
#This was from the forum authored by rivermaker, its short but I would like to see its functionality grow.


n = 317584931803

f = 3


while ( n > 1 ):
    if n % f == 0:
        n /= f
    else:
        f += 2


print ('largest factor is', f)
