<<<<<<< HEAD
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
=======
#Assignment 1
#Exercise 1

#diet = ''
#fruit = ['Banana', 'Cherry', 'Orange', 'Mango', 'Strawberry']
#fruit.sort()
#for i in fruit:
    #diet += i + ' + '
#print diet

#Define the string to be inserted between each element of the list 'fruit'.
space = ' + '
#Populate the list fruit with some arbitrary fruits.
fruit = ['Banana', 'Cherry', 'Orange', 'Mango', 'Strawberry']
fruit.sort()
#This command takes elements from the list fruit and inserts the string
#'space' between them.
diet = space.join(fruit)
#Print the result.
print diet
>>>>>>> cdb5a16dc9097fa65d176e771de3fc775508a7f4
