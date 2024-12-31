thistuple = ("apple", "banana", "cherry")

for x in thistuple:
  print(x)

print("***** for loop with range *****")

for i in range(len(thistuple)):
  print(thistuple[i])

# Javascript for loop
# for (let i = 0; i < 5; i++) {
#   text += "The number is " + i + "<br>";
# }

# step 1 -> initialize => i = 5
# step 2 -> condition => i >= 0
# step 3 -> increment/decrement => i+=1(i = i + 1) /i-=1(i = i - 1)

print("**** while loop ******")
# while loop
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1


# two methods
numtuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
# count(val)
x = count(3)
print(x)

# index(val)
x = index(8)
print(x)




