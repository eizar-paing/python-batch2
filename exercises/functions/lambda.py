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


models = [
  {'make': 'Nokia', 'model': 216, 'color': 'Black'}, 
  {'make': 'Mi Max', 'model': 2, 'color': 'Gold'}, 
  {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]

sorted_models = sorted(models, key=lambda x: x['color'])
# models.sort(key=lambda x: x['color'])
print(sorted_models)

# lambda x = {'make': 'Nokia', 'model': 216, 'color': 'Black'} => 'Black'
# lambda x = {'make': 'Mi Max', 'model': 2, 'color': 'Gold'} => 'Gold'
# lambda x = {'make': 'Samsung', 'model': 7, 'color': 'Blue'} => 'Blue'


# 'Black', 'Blue', 'Gold'
# {'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': 2, 'color': 'Gold'}











