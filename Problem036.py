import math

p = []
b= []
for z in range(1,1000000):
    x = str(z)
    y = x[::-1]
    xb = str(bin(z)[2:])
    yb = xb[::-1]
    if x == y and xb == yb:
        b += [x,xb]
        p += [x]
#print("p: ",p)

c = 0
for g in p:
    print(g)
    c += int(g)
print(c)
