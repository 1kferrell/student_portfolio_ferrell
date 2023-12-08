##Kyler Ferrell##
##Last Revised 12/02/2023##
##Basic Function_Portfolio Assignment##
##This program uses a function to add to integers##


##MY NOTES: add_nums gets defined as a function and takes to positional arguments x & y##
##MY NOTES: Within this function, the addition variable does the 'add' calculation for those arguments x & y##
##MY NOTES: The addition variable gets returned, so when it is called, it will execute##
##MY NOTES: Outside the function, x & y become initialized to their respective integers##
##MY NOTES: The addition variable then gets initialized to the add_num function WITH the positional arguments##
##MY NOTES: The print statment then prints (addition) which calls that function to do the math WITH those initialed arguments(3,6)##
##MY NOTES: The answer should be '9'##
def add_nums(x,y):
  addition = x + y
  return addition
x = 3
y = 6
addition = add_nums(x,y)

print(addition)