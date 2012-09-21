#Assignment 1
#Exercise 2

#String to convert is created.
person = 'fistName middleName lastName'
#A list is created with each name as an object in the order shown above.
list_person = person.split()
#The middle object is assigned to a variable as a string.
middle_name = list_person[1]
#The first character of the middle name is taken as the middle initial and a
#period is concatenated to it.
list_person[1] = middle_name[0] + '.'

#full_name = list_person[0].capitalize() + ' ' + middle_initial.capitalize() + ' ' + list_person[2].capitalize()

#The 'full_name' string is created from the objects in the list.
full_name = ' '.join(list_person)

print full_name
