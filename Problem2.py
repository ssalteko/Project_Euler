#Problem 2 for Project Euler

#Sum the even fibionocci numbers below 4M.

def EvenFibSum(n):
	f1,f2,EFS = 1,1,0
	while (EFS < n):
		EFS += (f1 + f2)
		f1, f2 = f1 + 2 * f2, 2 * f1 + 3 * f2
	return EFS
