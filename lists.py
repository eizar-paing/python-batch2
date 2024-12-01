import array

list = ["apple", "cherry", "orange", 3, 4]
array_a =  array.array('i', [2, 3, 4, 5])

#list
fruits = ["apple", "cherry", "orange"] 

#Access list items
print(fruits[2])
print(fruits[:2])

#Check if item exists
if "apple" in fruits:
  print("Yes, 'apple' is in the fruits list")

#Change items
fruits[0] = "Pineapple"

print(fruits)
