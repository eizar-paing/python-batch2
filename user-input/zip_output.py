names = ["John", "Charles", "Mike"]
scores = [85, 92, 78]
grades = ["B", "A", "C"]

# Name      Score    Grade
# John      85       B
# Charles   92       A
# Mike      78       C

print(f"{'Name':<10} Scrore")
print("..................")
# [["John",85], ["Charles", 92], ["Mike", 78]]
for name, score in zip(names, scores):
  print(f"{name:<10} {score}")
print("..................")





