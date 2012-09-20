#September 19th 2012
#Assignment 1
#Exercise 2

person = 'fistName middleName lastName'
list_person = person.split()
middle_name = list_person[1]
middle_initial = middle_name[0] + '.'

full_name = list_person[0].capitalize() + ' ' + middle_initial.capitalize() + ' ' + list_person[2].capitalize()

print full_name
