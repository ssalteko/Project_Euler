g = ""
h = 1

for x in range(1,1000000):
    g += str(x)
h = int(g[1-1])*int(g[10-1])*int(g[100-1])*int(g[1000-1])*int(g[10000-1])*int(g[100000-1])*int(g[1000000-1])
print(h)
