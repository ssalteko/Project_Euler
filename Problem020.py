#Project Euler Problem 20
#The task is to sum the digits of 100!
#I created two functions, one to calculate the value of n!, 
#The other function changes the number to a string, then grabs each digit and
#adds it to the total sum.


def factorial(n):
    m = n
    while n != 1:
        m *= n-1
        n -= 1
    return m

def sumanum(n):
    m = str(n)
    b = 0
    for x in range(0,len(m)):
        b += int(m[x])
    return b


print(sumanum(factorial(100)))
