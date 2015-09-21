#This is problem 22 from Project Euler
#The goal is to find the largest product of 4 adjacent numbers
#in a given matrix.

#Solution Authored on 9/20/2015 by Stephen J. Saltekoff.
    

def HSnipNProd(n,matrix):
    '''This searches a matrix for the largest sum of n adjacent values.'''
    M = 0
    rows = len(matrix)
    cols = len(matrix[0])

    if n > rows:
        return False
    if n > cols:
        return False

    for x in matrix:
        i = 0
        nn = n
        while i <= len(x)-n:
            t = 0
            m = 1
            while t < n:
                m *= x[i+t]
                t += 1
            if m > M:
                M = m
            i += 1
            nn += 1
    return M

def DSnipNProd(n,matrix):
    '''This searches a matrix for the largest sum of n adjacent
    diagonal and forward values.'''
    M = 0
    rows = len(matrix)
    cols = len(matrix[0])

    if n > rows:
        return False
    if n > cols:
        return False
    i = 0
    while i <= rows -n:
        
        j = 0
        while j <= cols -n:
            m = 1
            t = 0
            while t < n:
                m *= matrix[i+t][j+t]
                t +=1
            if m > M:
                M = m
            j += 1
        i += 1
    return M
    

def ReverseM(m):
    Rmatrix = []
    for x in m:
        y = x[::-1]
        Rmatrix += [y]
        #print(y,Rmatrix)
    Rmatrix = tuple(Rmatrix)
    return Rmatrix
    

#tmatrix =((1,2,3,4,5,6,7,8),(9,10,11,12,13,14,15,16),(17,18,19,20,21,22,23,24),
#         (25,26,27,28,29,30,31,32),(33,34,35,36,37,38,39,40),
#         (41,42,43,44,45,46,47,48),(49,50,51,52,53,54,55,56),

matrix =((8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91,8),
(49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0),
(81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65),
(52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91),
(22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80),
(24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50),
(32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70),
(67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21),
(24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72),
(21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95),
(78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92),
(16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57),
(86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58),
(19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40),
(4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66),
(88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69),
(4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36),
(20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16),
(20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54),
(1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48))

for x in matrix:
    for y in x:
        y = int(y)

#by passing a transposed matrix into HSnipSum we will find the largest column sum.
#Ttmatrix = tuple(zip(*tmatrix))
#Rtmatrix = ReverseM(tmatrix)

Tmatrix = tuple(zip(*matrix))

Rmatrix = ReverseM(matrix)





#print(matrix,Tmatrix)
t =(HSnipNProd(4,matrix),HSnipNProd(4,Tmatrix),DSnipNProd(4,matrix),DSnipNProd(4,Rmatrix))
#print(matrix[0][0],matrix[1][1],matrix[2][2],matrix[3][3])

print(max(t))

