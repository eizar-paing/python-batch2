class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
    
   
class Teacher(Person):
  def __init__(self, fname, lname, address):
    super().__init__(fname, lname)
    self.address = address

  def printname(self):
    super().printname()
    print("Address : ", self.address)

x = Student("Mike", "Olsen", 2024)
x.printname()
x.welcome()

y = Person("John", "Doe")
y.printname()

z = Teacher("Mary", "Brown")
z.printname()
