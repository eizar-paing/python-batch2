# while loop

x = 5
while x < 10:
  print("5 is less than 10.")
  x = x + 1 # x += 1

# continue statement

x = 6
while x < 10:
  x += 1
  if (x == 8):
    continue
  print("x ", x)
  # x += 1 # may cause infinite loop
  
# trace for continue
# 6<10 = true => x = 6+1 = 7 => (x == 8)? = print x  => 7
# 7<10 = true => x = 7+1 = 8 => (x == 8)? => continue
# 8<10 = true => x = 8+1 = 9 => (x == 8)? => printt x => 9
# 9<10 = true => x = 9+1 = 10 => (x == 8)? => print x => 10

# break statement
x = 6
while x < 10:
  if (x == 8):
    break
  print("x ", x)
  x += 1

print("end of while loop")

# for loop
fruits = ["apple", "orange", "banana"]
for a in fruits:
  print(a)
  if a == "orange":
    break
else: 
  print("end of for loop inside")
print("end of for loop outside")

print("-------------------------")
for a in fruits:
  if a == "orange":
    continue
  print(a)
else:
  print("end of for loop 2 ")

# pass statement
for x in range(5):
  # print(x)
  pass
