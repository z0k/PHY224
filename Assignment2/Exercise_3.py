#Populate a list with duplicate entries.
items = range(5, 11) + range(1, 6) + range(9, 20)
print "The original list is: ", items

#Define the list 'new_items' to hold duplicates.
new_items = []
#I is the first element to compare.
for i in items:
    #Count is reset after each loop through the second element for comparison.
    #That is, the count starts anew for the next i element to check against j.
    count = 0
    #The second element to compare to the first.
    for j in items:
        #Test condition for duplicates.
        if i == j:
            #Every time a duplicate is found increase the counter by 1.
            count += 1
    #If the count is greater than 1, that means that a duplicate exists.
    if count > 1:
        #Populate the list new_items with the duplicates.
        new_items.append(i)
#Duplicates from the list are removed using the set functin.
new_items = sorted(set(new_items))

print "The following are the duplicate entries in the list: ", new_items
