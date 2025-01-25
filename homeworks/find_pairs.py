nums = [1, 2, 3, 4]

user_input = input("Enter a target number: ")
target_value = int(user_input)
result = []

for n in nums:
    diff = target_value - n
    if diff in nums and (diff, n) not in result and (n, diff) not in result:
        result.append((n, diff))


print(result)