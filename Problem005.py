#Project Euler, Problem 5


def primefactors(n):
    '''find the prime factors of a number, not including 1 and itself'''
    pdivs = []
    i = 3
    if n == 1 and i <= n**(1/2):
        pdivs = 1
        return pdivs

    if n == 2:
        pdivs = [1,2]
        return pdivs

    while n != 1:
        while n%2 == 0:
            pdivs += [2]
            n //= 2
            

        
        while n%i == 0:
            pdivs += [i]
            n //= i
        i += 2
       
        
    if len(pdivs)==0:
        pdivs = [n]
        return pdivs
    return pdivs

def sortncount(n):
    '''pass an array through to be sorted and counted as a dictionary'''
    dictr = {}
    for element in n:
        if element in dictr:
            dictr[element] += 1
        else:
            dictr[element] = 1
    return dictr


def highestfreq(n):
    '''returns a dictionary consisting of keys that are in each dictionary, and their highest frequency'''
    dictr = {}
    for x in n:
        for p,b in x.items():
            #print(p,b)
            if p not in dictr:
                dictr[p] = 1
            if dictr[p]<b:
                dictr[p] = b
    return dictr

def powerdict(n):
    '''This raises each dict key to a power of its value'''
    y = 1
    for x in k:
        y *= x**k[x]
    return y

l = []

for x in range(1,21,1):
    l += [sortncount(primefactors(x))]


k = highestfreq(l)

print(powerdict(highestfreq(l)))
