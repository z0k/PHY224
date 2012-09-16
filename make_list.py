mylist = []

element = ''
while element != 'end':
    element = raw_input("Enter an element for the list. To finish, type 'end'.")
    mylist.append(element)
    
for element in mylist:
    #print element
    if element.isalpha() == False:
        print element


