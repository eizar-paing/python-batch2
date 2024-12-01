nameList = ["John", "Rose", "David", "Mary"]

def searchName(name):
  i = 0
  result = False
  while i < len(nameList):
    if nameList[i] == name:
      result = True
      break
    else:
      i += 1
  if result:
    print("There is user name!")
  else:
    print("Not found user name!")
  
  print("end of while loop")

isTrue = True
while isTrue:
  username = input("Enter user name: ")
  searchName(username)
  answer = input("Do you want to search again? Enter yes/no : ")
  if answer == "yes":
    isTrue = True
  else:
    isTrue = False

    
