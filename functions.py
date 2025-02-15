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

# (1, 2, 3, 4)
def addtionMutipleNumbers(*num):
  result = 0

  # for x in num:
  #   result += x
  for x in range(len(num)):
    result += num[x]
  print("total result : ", result)

addtionMutipleNumbers(1, 2, 3, 4)

# Arbitary Keyword Arguments
def my_function(**kid):
  for key, value in kid.items():
    print(f"{key} of kid is {value}.")

# (key, value)

my_function(fname = "Tobias", lname = "Refsnes")
my_function(fname = "Tobias", lname = "Refsnes", mname = "")

# Default Parameter Value
def my_function2(fname = "No", lname  = "No"):
  # print("My first name is ", fname, " and last name is ", lname)
  print(f"My first name is {fname} and last name is {lname}")

my_function2("John", )
my_function2()

# *** list parameter and arbitary arguments
def my_function_with_list_parameter(food):
  for x in food:
    print(x)

my_function(["apple", "banana", "cherry"])

def my_function_with_arbitary_arguments(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


