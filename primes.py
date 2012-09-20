

def primes(n):

    #Initialize list of numbers from 2 to 100.
    numbers = range(2, n + 1)
    #print numbers

    number = []

    #Loop to go through every integer from 2 to 100 in the list numbers.
    for i in numbers:
        #Initialize list of numbers from 2 to 100.
        divisors = []
        #Nest loop to go through every integer up to i in outer loop.
        for j in range(1, i + 1):
            #Test for divisors of each number i
            if i % j == 0:
                divisors.append(j)
        #Test to check for number of divisors for each number i. If there are
        #only 2 divisors, then that number must be prime.
        if len(divisors) == 2:
            #print i
            number.append(i)
    return number
num = int(input('Enter a positive integer: '))
print primes(num)
