##Kyler Ferrell##
##While True loop List##
##This program will promt the user to enter a 5 character name and add it to a list or enter 'q' to quit the programs## 
##The user will get an error if the input is not entered correctly##

name_list = []

while True:
  name = input("Enter a name with exactly 5 letter (or 'q' to quit): ")
  if name.lower() == 'q':
    break
  elif len(name) ==5:
    print(f"Name added: {name}")
    name_list.append(name)
    print(f"Your name list is: {name_list}")
  else:
    print(f"Your name entry {name} has to contain 5 letter only")
    print(f"Please try again")
