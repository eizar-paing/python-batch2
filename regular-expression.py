import re
import camelcase

txt = "ab123"

# x = re.search(r'^(?=(?:.*\d){3}$).{3,}$', txt)

x = re.search(r'(.+){3}\d{3}', txt)

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")


# phone number
num = "091-1234567890"
x = re.search(r'^\d{2,3}-\d{9,10}$', num)

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")

# email format
# aBc.100%-123@gmail.com
# aBc.100%-123@abc.co.mm

# zip code
# 123-1234

# password format
# at least 8
# characters and digits

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))