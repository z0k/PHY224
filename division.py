a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

#Check to see if one divides the other.
if a % b == 0:
    print 'Yes'
elif b % a == 0:
    print 'Yes'
else:
    print 'No'
    
