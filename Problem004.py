#Problem 4 from Project Euler
#Find the largest palendrome between two three digit numbers.

print(max([x*y for x in range(900,1000) for y in range(900,1000) if str(x*y) == str(x*y)[::-1]]))

#This was found on the Project Euler forum authored by iang 9/5/2015.

#I like the shortness of the one line but there are several things happening.

#You must know that said number would be between 900 and 999.
#Reversing a string is super easy with "str(the_thing)[::-1}"
#The max function takes the max value of an array, cool.
