#Assignment 1
#Exercise 3

W = int(input('Please enter your weight in pounds: '))
H = raw_input('Please enter your height in feet and inches: ')
#The " is first trimmed from the string H (H[:-1] removes the last character
#in the string)
H_num = H[:-1]

#The string is split in two at the ' symbol. This is to try to separate the
#feet from the inches measurements.
height = H_num.split("'")

#Integer values are extracted from the string and feet are converted to inches.
feet = int(height[0]) * 12
inches = int(height[1])

#Total height is calculated in inches.
total_height = feet + inches

#Formulate for body mass index.
BMI = 703. * W / (total_height ** 2)
print "Your BMI is ", BMI
