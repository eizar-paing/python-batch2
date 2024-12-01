
x = "awesome"

def myfunc():
  global y 
  y = "amazing"
  print("inside fun: Python is " + y)


myfunc()

print("outside fun: Python is " + y)




