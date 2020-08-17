class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
    self.graduationyear = 2019

#da ke thua
class First:
    def getClass(self):
        print("Class Fist")

class Second:
    def getClass(self):
        print("Class Second")
        
class Third(First, Second):
    def getClass(self):
        super().getClass()

third = Third()
third.getClass()

# Kết Quả:
# Class Fist

#super----------------------------
class Foo:
    name = 'Foo'
    def getName(self):
        print("Class: Foo")
        
class Bar(Foo):
    name = 'Bar'
    def getName(self):
        print("Atribute name = " + super().name)
        super().getName()

Bar().getName()
# Ket qua:
# Atribute name = Foo
# Class: Foo