def double(num):
  return num * 2

def triple(num):
  return num * 3

def quadruple(num):
  return num * 4

x = double(2)
y = triple(3)
z = quadruple(4)


# using lambda function

def myfunc(num):
  return lambda a : num * a

n1 = myfunc(5) # lambda a : 5 * a

print(n1(2)) # double
print(n1(3)) # triple
print(n1(4)) # quadruple






