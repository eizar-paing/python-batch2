# ==
# !=
# <
# >
# <=
# >=
a = 4
b = 4

if a > b:
  print("a is greater than b")
elif a == b:
  print("a and b are same")
else: 
  print("a is less than b")

user_mark = input("Enter your mark : ")
mark = int(user_mark)

if mark >= 80:
  print("Grade A")
elif mark >= 60:
  print("Grade B")
elif mark >= 40:
  print("Grade C")
elif mark >= 20: 
  print("Grade D")
else: 
  print("Grade E")

print("end of condition!")

if mark >= 80:
  print("A")
else:
  if mark >= 60:
    print("B")
  else:
    if mark >= 40:
      print("Grade C")
    else:
      if mark >= 20:
        print("Grade D")
      else:
        print("Grade E")


# short hand if
if a == b: print("true")

if a == b:
  print("true")
else:
  print("false")

# short hand of if ... else
print('true') if a == b else print("false")

print('a') if a > b else print('equal') if a == b else print('b')

# (work of if) if a == b else ((work of if) if a == b else (work of else))
# x if a>b else x if a>b else y

# x = work of if
# y = work of else
# z = work of if inside else
# t = work of else inside else

# x if condition1 else z if condition2 else t
# x if con else x if con else x if con else x if con else x if con else x if con else y

# logical operators => and, or, not
a = 100
b = 200
c = 300


# false and true => false
if a > b and c > a: 
  print("true")
else:
  print("false")

# false or true => true
if a > b or c > a:
  print("true")
else:
  print("false")

# not false => true
if not a > b: 
  print("true")

if not a != b:
  ptint("true")

# pass statement
if a == b:
  pass
print("testing")

# Nested if

if a > b:
  if a > c:
    print("a is greater than b and c")
  else:
    print("a is greater than b and not c")

if mark >= 80:
  print("Grade A")
elif mark >= 60:
  print("Grade B")
elif mark >= 40:
  print("Grade C")
elif mark >= 20: 
  print("Grade D")
else: 
  print("Grade E")



mark = 90
if mark >= 80:
  print("A")
else:
  if mark >= 60:
    print("B")

# result => 
# A
# B











