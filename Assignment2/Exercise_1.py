#Assignment 2
#Exercise 1


#Define the asterik triangle function.
def triangle(base):

    #The value i represents the number of asteriks to print per line.
    i = 0
    #This loop executes until the base reaches -1. Because the triangle
    #is right justified, the base is actually the number of spaces.
    while base > -1:
        #Print 'base' number of spaces, followed by 'i' asteriks.
        print ' \t' * base + '*\t' * i
        #print a vertical tab after each line.line
        print '\v'
        #The number of spaces goes down while the number of asteriks goes up
        #with each line.
        base -= 1
        i += 1

#Prompt the user for the number of asteriks you would like.
#In actuality this is the number of spaces but it achieves the same effect. 
base = int(input("Enter the number of asteriks for the base: "))
triangle(base)
