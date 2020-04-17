#Problem 2 for Project Euler

#Sum the even fibionocci numbers below 4M.

def EvenFibSum(n):
	'''returns the sum of even fibionocci numbers below n)'''
	f1,f2,EFS = 1,1,0
	while (EFS < n):
		EFS += (f1 + f2)
		f1, f2 = f1 + 2 * f2, 2 * f1 + 3 * f2
	return EFS

print(EvenFibSum(10000))

#This is interesting and was pulled from Project Euler on 9/4/2015 Authored by Begoner.
#Here is their explanation:
#This may be a small improvement.  The Fibonacci series is:

#1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610...

#Now, replacing an odd number with O and an even with E, we get:

#O, O, E, O, O, E, O, O, E, O, O, E, O, O, E...

#And so each third number is even.  We don't need to calculate the odd numbers.  Starting from an two odd terms x, y, the series is:

#x, y, x + y, x + 2y, 2x + 3y, 3x + 5y

#And in Python, my solution is:
