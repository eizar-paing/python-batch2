# Print the following pattern

# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1

row = 5
col = 5

#range(start, stop, step)

for x in range(row, 0, -1):
  # x
  for y in range(x, 0, -1):
    print(y, end=' ')
  print()




