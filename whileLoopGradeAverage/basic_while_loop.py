##Kyler Ferrell##
##Last Revised 12/10/2023##
##While_Loop_Portfolio_Assignment##
##TThis program will promt the user to input data to find the sum. If data is null the program will end.#

#Ths while True statement prompts the user to enter a number#
#The if statement makes a condition for that number to be between 0 and 100 and if neither than program will end
#This get repeated for 3 different numbers
while True:
  number = int(input("Enter the number grade: "))
  if number >= 0 and number <= 100:
    break
  else:
    print("Error: Grade must be between 0 and 100")
  print(number)

while True:
  number2 = int(input("Enter the number grade: "))
  if number >= 0 and number <= 100:
    break
  else:
    print("Error: Grade must be between 0 and 100")
  print(number2)

while True:
  number3 = int(input("Enter the number grade: "))
  if number >= 0 and number <= 100:
    break
  else:
    print("Error: Grade must be between 0 and 100")
  print(number3)


#The average variable adds the 3 inputs and divides them to get the average score
average = (number + number2 + number3) / 3
print("The average score is: "+str(average))

