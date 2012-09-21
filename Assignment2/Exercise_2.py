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


#Define the exponential function
def compute_e(num_terms):
    #Total is initialized to 1 because 1/1! = 1, i.e. the first term of the
    #series.
    total = 1
    #The for list runs 'num_terms' times. A 1 is added because it terminates
    #up to but not including the end-point.
    for i in range(1, num_terms + 1):
        #Care is taken to use a floating number to perform the addition.
        #The factorial function is called to compute the series.
        total += 1. / factorial(i)
        #print total
    return total

num = int(input("Enter the number of terms for the approximation: "))

#The series function is called and the result is printed.
print compute_e(num)
