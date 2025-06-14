isTrue = True

while isTrue:
  num = input("Enter a number:")
  try:
    result = float(num)
    print(f"the result is {result}")
    isTrue = False
  except:
    print("The input you entered is not number. cannot change to float!")



