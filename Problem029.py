d = {}
a = 2
b = 2

while a<=100:
    d[a**b] = 1
    while b<=100:
        d[a**b] = 1
        b+= 1
    a += 1
    b = 2
l = []
for x in d:
    l += [x]
#print(d)
print(len(l))
        
