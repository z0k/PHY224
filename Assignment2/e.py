#Assignment 2
#Exercise 2

#Define the factorial function.
def factorial(a):
    #fac is the factorial product.
    fac = 1
    #Test to see if the number is positive.
    if a < 0:
        print "Number must be positive."
    else:
        #Go through the list of numbers up until the input and multiply
        #them all together.
        for i in range(1, a + 1):
            fac *= i
        return fac

e = 0

num = int(input("Enter the number of terms of the series: "))

for i in range(0, num + 1):
    e += 1. / factorial(i)

print e
