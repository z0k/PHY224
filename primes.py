#num = int(input('Enter a positive integer: '))

divisors = []
numbers = range(2,101)
for i in numbers:
    for j in range(1,i+1):
        if i%j == 0:
            divisors.append(j)
    if len(divisors) == 2:
        print i
