# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range(1, 6):
  for j in range(i):
    print(j+1, end='')
  print('')

# i = 1 => 
  # j = 0-0 => i = 1
# i = 2 => 
  # j = 0 => i = 2
  # i = 1 => i = 2
# i = 3 => 
  # j = 0 => i = 3
  # j = 1 => i = 3
  # j = 2 => i = 3


# 1          => 1 
# 2 2        => 2
# 3 3 3      => 3
# 4 4 4 4    => 4
# 5 5 5 5 5  => 5

for i in range(1, 6):
  for j in range(i):
    print(i, end='')
  print('')

# i = 1 => 
  # j = 0-0 => 1
# i = 2 => 
  # j = 0 => 2
  # i = 1 => 2
# i = 3 => j = 0-2 => 3 3 3
# i = 4 => j = 0-3 => 4 4 4 4

# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5


b = 0
for i in range(5, 0, -1):
  b += 1
  for j in range(i):
    print(b, end=' ')
  print('')

# 6 6 6 6 6 6
# 5 5 5 5 5
# 4 4 4 4 4
# 3 3 3
# 2 2
# 1

# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

# i = 1 => 4 1
# i = 2 => 3 2
# i = 3 => 2 3
# i = 4 => 1 4
# i = 5 => 0 5

# 4 3 2 1 0
# 1 2 3 4 5 => 5-1 = 4
#              5-2 = 3
#              5-3 = 2
#              5-4 = 1
#              5-5 = 0


# 5 5 15 75 525 ....

# 3 6 9 12 ?
# 1 2 3 4 5
# 3*1 3*2 3*3 3*4 3*5 => 3*n



#         1
#       1 2
#     1 2 3 
#   1 2 3 4
# 1 2 3 4 5

for i in range(1, 6):
  for j in range(5-i):
    print(' ', end= '')
  for k in range(1, i+1):
    print(k, end = '')
  print()
  
# 1
# 3 3
# 5 5 5
# 7 7 7 7
# 9 9 9 9 9

# 1 3 5 7 9  => (1*2)-1 =1,  (2*2)-1=3, (3*2)-1 =5 => (n*2)-1
# 1 2 3 4 5


# i = 1 (line 1)
# j = 1->1 = 1 (numbers of display)

# i = 2 (line 2)
# j = 1->2 = 1
# j = 1->2 = 2

# i = 3 (line 3)
# j = 1->3 = 1
# j = 1->3 = 2
# j = 1->3 = 3

# i = 1, j = 1 => 1
# i = 2, j = 1, 2 => 3 3
# i = 3, j = 1, 2, 3 => 5 5 5



for i in range(1, 6): # for line
  for j in range(1, i+1): # for times in each line
    print((i*2)-1, end='')
  print()

# 1 2 4 7 11 16
# 1 2 3 4 5 6

# (1 * 2)/2 = 1
# (1 * 3)/2 = 2
# (2 * 4)/2 = 4

# 1
# 2 2
# 4 4 4
# 7 7 7 7

num = 1
for i in range(1, 6): # for line
  for j in range(1, i+1): # for times in each line
    print(num, end='')
  print()
  num += i


# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

for i in range(5, 0, -1):
  for j in range(i, 0, -1):
    print(j, end='')
  print()

# 1  => 1 => 2
# 3 2  => 2 => 4
# 6 5 4 => 3 => 7
# 10 9 8 7 => 4 => 11

# 1 => 1 => start1 = 1, stop1 = 2
# 3 2 => 2 => start2 = stop2 + 2 -1, stop2 = start1 + 1
# 6 5 4 => 3 = start3 = stop3 + 3 -1, stop3 = start2 + 1
# 10 9 8 7 => 4, start4 = stop4 + 4 -1, stop4 = start3 + 1
print("********")

# 1 => 1 => start = 1, stop = 2
# 3 2 => 2 => start = stop, stop = stop + i
# 6 5 4 => 3 => start = stop, stop = stop + i
# 10 9 8 7 => 4 => start = stop, stop = stop + i

start = 1
stop = 2
num = stop
for i in range(2, 6):
  for j in range(start, stop):
    num = num - 1
    print(num, end='')
  start = stop
  stop = stop + i
  num = stop
  print()

# i = 1 => start = 1, stop = 2, j = 1->2 => num = 2 => num - 1 = 1
# i = 2 => start = 2, stop = 4, j = 2->4 => num = 4 => num -1 = 3 , num -1 = 1

print("********")
# 1 2 3 4 5 => 1
# 2 2 3 4 5 => 2
# 3 3 3 4 5 => 3
# 4 4 4 4 5 => 4
# 5 5 5 5 5 => 5

for i in range(1, 6):
  for j in range(1, 6):
    if j <= i:
      print(i, end='')
    else: 
      print(j, end='')
  print()

# *
# * *
# * * *
# * * * *
# * * * * *

#         *
#       * *
#     * * *
#   * * * *
# * * * * *


# * * * * *
# * * * *
# * * *
# * * 
# * 


# * * * * *
#   * * * *
#     * * *
#       * *
#         *


# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * * 
# * 


#         *
#       * *
#     * * *
#   * * * *
# * * * * *
#   * * * *
#     * * *
#       * *
#         *



#     *           => 1
#    * *          => 2
#   *   *         => 3
#  *     *        => 4
# *       *       => 5
#  *     *
#   *   *
#    * *
#     *

#     *           => 1
#    * *          => 2
#   * * *         => 3
#  * * * *        => 4
# * * * * *       => 5
#  *     *
#   *   *
#    * *
#     *
print("stars with space ......... ")
for i in range(1, 6):
  #for space
  for j in range(1, 6-i):
    print(" ", end="")
  for k in range(i):
    if (i<=2):
      print("* ", end="")
    else:
      if k == 0 or k == i - 1:
        print("* ", end="")
      else:
        print("  ", end="")
  print()
  

# solution 1
rows = 5
i = 1
while i <= rows:
    j = rows
    while j > i:
      # display space
      print(' ', end=' ')
      j -= 1
    print('*', end=' ')
    k = 1
    while k < 2 * (i - 1):
        print(' ', end=' ')
        k += 1
    if i == 1:
        print()
    else:
        print('*')
    i += 1

i = rows - 1
while i >= 1:
    j = rows
    while j > i:
      print(' ', end=' ')
      j -= 1
    print('*', end=' ')
    k = 1
    while k <= 2 * (i - 1):
      print(' ', end=' ')
      k += 1
    if i == 1:
      print()
    else:
      print('*')
    i -= 1

# solution 2
n = 5  # Controls the height of the top half

# Top half
for i in range(1, n + 1):
  print(" " * (n - i), end="")          # Leading spaces
  if i == 1:
    print("*")
  else:
    print("*" + " " * (2*i - 3) + "*")

# Bottom half
for i in range(n - 1, 0, -1):
  print(" " * (n - i), end="")          # Leading spaces
  if i == 1:
    print("*")
  else:
    print("*" + " " * (2*i - 3) + "*")


# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10

num = 1
for i in range(1, 5):
  for j in range(i):
    print(num, end=" ")
    num += 1
  print() 