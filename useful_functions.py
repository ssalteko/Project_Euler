def primefactors(n):
    '''returns a list of prime factors of n, as an array'''
    pdivs = []
    i = 3
    if n == 1 and i <= n**(1/2):
        pdivs = 1
        return pdivs

    if n == 2:
        pdivs = [1,2]
        return pdivs

    if n != 1:
        while n%2 == 0:
            pdivs += [2]
            n //= 2
            #print(pdivs)

        
        while n%i == 0:
            pdivs += [i]
            n //= i
        i += 2
        #print(pdivs)

    if len(pdivs)==0:
        pdivs = [n]
        return pdivs
    return pdivs


def sortncount(n):
    '''pass an array through to be sorted and counted as a dictionary'''
    dict = {}
    mylist = n
    for element in mylist:
        if element in dict:
            dict[element] += 1
        else:
            dict[element] = 1
    return dict
