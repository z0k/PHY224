my_list = [1,2,3,4,5,6,7]

num = int(raw_input("Enter a number: "))

#for i in range(0,len(my_list)):
    #if my_list[i] == num:
        #my_list.remove(my_list[i])
        #print my_list
    #if i == len(my_list)-1:   
        #print my_list

if num in my_list:
    my_list.remove(num)
print my_list


