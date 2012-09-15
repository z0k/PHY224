def median(x,y,z):
    if x == max(x,y,z):
        med = max(y,z)
    if y == max(x,y,z):
        med = max(x,z)
    if z == max(x,y,z):
        med = max(x,y)
    return med

a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
c = float(input("Enter the length of the third side: "))

#Check to see which side is the hypotenuse
h = max(a,b,c)

side1 = min(a,b,c)
side2 = median(a,b,c)

if h**2 == (side1**2 + side2**2):
    print "The triangle is a right angled triangle."
else:
    print "The triangle is not a right angled triangle."
