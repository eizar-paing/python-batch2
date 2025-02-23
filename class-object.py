class Student:

  def __init__(self, p_name, p_age):
    self.name = p_name
    self.age = p_age

student1 = Student("Mg Mg", 12)
student2 = Student("May", 13)
student3 = Student("Nyi Nyi", 12)

print(student1.name, " and ", student1.age)
print(student2.name, " and ", student2.age)
print(student3.name, " and ", student3.age)