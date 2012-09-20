#September 19th 2012
#Assignment 1
#Exercise 3

W = int(input('Please enter your weight in pounds: '))
H = raw_input('Please enter your height in feet and inches: ')
H_num = H[:-1]
print H_num

height = H_num.split("'")

feet = int(height[0]) * 12
inches = int(height[1])

total_height = feet + inches

print total_height

#>>> str = "h3110 23 cat 444.4 rabbit 11 2 dog"
#>>> [int(s) for s in str.split() if s.isdigit()]
