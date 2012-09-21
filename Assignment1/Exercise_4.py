#Assignment 1
#Exercise 4

from time import strptime
from datetime import date

#User inputs a string in the form 'Month Day#'
user_date = raw_input("Enter the date as a month followed by the day: ")
#Split the input string into a list containing two objects month and day.
list_date = user_date.split()

#list_date[0] is the string indicating the month.
#month_number = int(strptime(list_date[0], '%B').tm_mon)

#Populate a list with the names of months.
month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

#The index number is extracted from the list of months in order to get the month number.
month_date = month_list.index(list_date[0])

#The day number is parsed from the original string inputted by the user.
day = int(list_date[1])

#The first day of the year is subtracted from the parsed date in terms of the number of days.
#1 is added to month_date because the indices begin at 0.
print "There have been", (date(2012, month_date + 1, day) - (date(2012, 1, 1))).days, "days since the beginning of the year."
