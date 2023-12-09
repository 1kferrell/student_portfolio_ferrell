##Kyler Ferrell##
##Last Revised 12/09/2023##
###calling multiple functions portfolio assignment##
##This program shows how multiple math functions can be called to execute different math problems#

##This addition function takes the x and y variables as positional arguments##
#The 'addition' variable within the function gets initalized to add x and y#
#The 'addition' then gets returned when the function is called##
def add_nums(x, y):
  addition = x + y
  return addition

#The x and y variables get initialized to integers#
x = 347
y = 184
#The addition variable then gets set to the function WITH the x and y parameters#
addition = add_nums(x, y)

def subtract_nums(y,x):
  subtraction = y - x
  return subtraction
subtraction = subtract_nums(y, x)

def multiply_nums(x, y):
  multiplication = x * y
  return multiplication
multiplication = multiply_nums(x,y)

def divide_nums(y, x):
  division = y / x
  return division
division = divide_nums(y,x)

##The print statements call all of the above functions in order##
#They all do their respective calculations and diplay the answers##
print(f"{x} plus {y} is {addition}")
print(f"{y} minus {y} is {subtraction}")
print(f"{x} times {y} is {multiplication}")
print(f"{y} minus {x} is {division}")