#The goal is to find the first triangular number with 500 divisors.
#Authored by Stephen J. Saltekoff

def triagonum(n):
    triagonum = n*(n+1)//2
    return triagonum

def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(n**(0.5) + 1)):
        if n % i == 0:
            yield int(i)
            if i != n / i:
                large_divisors.insert(0, n / i)
    for divisor in large_divisors:
        yield int(divisor)


##for x in range(1,10):
##    print(len(list(divisorGenerator(triagonum(x)))))
    
i = 1
b = 0
a = 0

while b <= 500:
    b = len(list(divisorGenerator(triagonum(i))))
    a = triagonum(i)
    i += 1

print(a)

