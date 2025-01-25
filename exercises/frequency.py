colorList = ["Red", "Green", "Red", "Blue", "Green", "Red"]

# Result : {"Red": 3, "Green": 2, "Blue": 1}

result = {}

colorSet = set(colorList)
print(colorSet)

for color in colorSet:
  count = colorList.count(color)
  result[color] = count

print(result)





