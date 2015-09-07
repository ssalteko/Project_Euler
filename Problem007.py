def nprime(n):
    '''returns the nth prime'''
    primes = [2,3,5,7,11,13]
    num = 15
    while len(primes) < n+1:
        if all(num % m != 0 for m in primes):
            primes.append(num)
        num += 2
    return primes[n]

#print(nprime[10000])
