import array


numbers = array.array('i', [1, 2, 3, 4, 5])

numbers.append(6)
numbers.insert(2, 10)
numbers[3] = 8

print(numbers)