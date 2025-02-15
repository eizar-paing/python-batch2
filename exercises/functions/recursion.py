def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result


res = tri_recursion(6)
print("Recursion Example Results:", res)

# tri_recursion(6) 
# if(k>0) => 6>0 => true 
#  => result = 6 + tri_recursion(5) 
# => result = 6 + 15 = 21 => return 21

# tri_recursion(5) 
# if (k>0) => 5 > 0 => true
# => result = 5 + tri_recursion(4)
# => result = 5 + 10 = 15 => return 15

# tri_recursion(4)
# if(k>0) => 4 >0 => true
#  => result = 4 + tri_recursion(3)
#  => result = 4 + 6 = 10 => return 10

# tri_recursion(3)
# if(k>0) => 3 >0 => true
#  => result = 3 + tri_recursion(2)
# => result = 3 + 3 = 6 => return 6

# tri_recursion(2)
# if(k>0) => 2 >0 => true
#  => result = 2 + tri_recursion(1)
#  => result = 2 + 1 = 3 => return 3

# tri_recursion(1)
# if(k>0) => 1 >0 => true
#  => result = 1 + tri_recursion(0)
#  => result = 1 + 0 = 1 => return 1

# tri_recursion(0)
# if(k>0) => 0 >0 => false
# else => result = 0 => return 0

# print
# 1
# 3
# 6
# 10
# 15
# 21