from numpy import *

a = input("Enter the length of one side: ")
b = input("Enter the length of another side: ")
theta = input("Enter the angle between the sides: ")

#Formula for area
A = (a*b*sin(theta))/2

print A
