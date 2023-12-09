##Kyler Ferrell##
##Last Revised 12/09/2023##
##function_inputs_portfolio assignment##
##This program uses a function to add to integers##

#The user is prompted to input integers for variables a and b#

a = int(input("Enter a number for a variable: "))
b = int(input("Enter a number for b variable: "))

#This function takes those variables as positional arguments##
#The formula variable within the function gets initalized to do the math with those a and b parameters#
#The forula then gets returned when the function is called##
def num_formula(a,b):
  formula = (a * b)**2 - 10
  return formula

#The formula variable then gets set to the function WITH the a and b#
formula = num_formula(a,b)

##The print statement calls the function, does the math, and displays the answer##
print(formula)