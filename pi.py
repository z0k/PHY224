num = int(input("Enter the number of terms in series to approximate pi: "))

n = 1
pi = 0
for i in range(0, num + 1):
    pi += (1. / n) * ((-1) ** i)
    n += 2
    print 4. * pi
