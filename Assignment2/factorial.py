#Tutorial 3
#Question 11

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


#num = int(input('Enter a positive number: '))
#print factorial(num)


#Define the exponential function
def compute_e(num_terms):
    #Total is initialized to 1 because 1/1! = 1, i.e. the first term of the
    #series.
    total = 1
    for i in range(1, num_terms + 1):
        total += 1. / factorial(i)
        #print total
    return total

num = int(input("Enter the number of terms for the approximation: "))

print compute_e(num)
