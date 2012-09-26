#Assignment 1
#Exercise 1

#Define the string to be inserted between each element of the list 'fruit'.
space = ' + '
#Populate the list fruit with some arbitrary fruits.
fruit = ['Banana', 'Cherry', 'Orange', 'Mango', 'Strawberry']
#This command combines the elements from the list fruit into the new string
#'diet', and inserts the string 'space' between them.
diet = space.join(fruit)
#Print the result.
print diet
