##Kyler Ferrell##
##Last Revised 12/10/2023##
##for_range_loop_Portfolio_Assignment##
##This program prompts the user to enter a series of numbers, then the for loops display the range of thos e numbers#

#x variable is initialized to an integer and user is promper to enter number start range
#y variable is initialized to an integer and user is promper to enter number end range
x = int(input("Enter a number start range: "))
y = int(input("Enter a number end range: "))

#This for loop sets a range for the positional arguments x and y, and a -1 since range counts 0
for count in range(x, y, -1):
  
  #The range of number are displayed
  print(count)