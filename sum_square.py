
def sum(a, b):
    total = 0
    for i in range(a,b+1):
        total += i**2
    return total

print sum(1,4)
