def PrimesSet(n):
    '''this lists primes below the value n'''
    m = [0] * n
    j = 3
    SetOfPrimes = [2]
    while j < n:
        if m[j] == 0:
            SetOfPrimes += [j]
            p = j
            while p < n:
                m[p] = 1
                p += j
        j += 2
    return SetOfPrimes

def IntShiftr(n):
    '''takes int abc and returns bca'''
    s = str(n)
    sh = str()
    for x in s:
        sh = s[-1]+s[0:-1]
        #print(sh)
        return int(sh)

ListOfPrimes = PrimesSet(1000000)
SetOfPrimes = set(ListOfPrimes)
b = set()
le = len(ListOfPrimes)
i = -1

while i < le-1:
    i += 1
    prime = ListOfPrimes[i]
    l = len(str(prime))
    c = set()
    #print(prime)
    if prime not in b:
        while l > 0:
            prime = IntShiftr(prime)
            c.add(prime)
            l -= 1
    d = set()
    for x in c:
        if x in SetOfPrimes: 
            d.add(x)
    if len(d) == len(c):
        #print(d)
        for y in d:
            b.add(y)
    #print(b)

print(len(b))    
        
        
        
