#Problem 22 from Project Euler
#The goal is to sum the product of all name values by thier index.
#Authored by Steve Saltekoff on 9/15/2015


def ReadToElmentValue(name,alphavalue):
    SumOfNameValues = 0
    for x in name:
        SumOfNameValues += alphavalue[x]
    return SumOfNameValues


alephbet = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
NameList =[]
SumOfNameValues = 0
NamesFromFile = open('p022_names.txt','r')

NamesFromFile = NamesFromFile.read()
NamesFromFile = NamesFromFile.split(',')

    
for name in NamesFromFile:
    name = name[1:-1]
    NameList += [name]

NameList.sort()
LengthOfNameList = len(NameList)

for i in range(0,LengthOfNameList):
    SumOfNameValues += ReadToElmentValue(NameList[i],alephbet)*(i+1)
print(SumOfNameValues)
    
