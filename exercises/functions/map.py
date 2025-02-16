
def myfunc(a):
  return len(a)

x = map(myfunc, ('apple', 'banana', 'cherry')) # [5, 6, 6]


# Using lambda function
nums = [2, 4, 6, 9, 11]
n = 4

result = list(map(lambda number: number * n, nums))
print(result)


# 2 * 2 => 4
# 4 * 2 => 8
# 6 * 2 => 12
# 9 * 2 => 18
# 11 * 2 => 22



