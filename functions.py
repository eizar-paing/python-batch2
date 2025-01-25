def addition(num1, num2, num3):
  x = num1 + num2 + num3
  print("result of addition : ", x)


addition(1, 2, 3)
addition(2, 3, 4)
addition(4, 7, 5)

def getName(fname, lname):
  x = fname + " " + lname
  print("Thank you ", x)
getName("John", "Smith")

# [1, 2, 3, 4]
def addtionMutipleNumbers(*num):
  result = 0

  # for x in num:
  #   result += x
  for x in range(num.len()):
    result += num[x]
  print("total result : ", result)

addtionMutipleNumbers(1, 2, 3, 4)




