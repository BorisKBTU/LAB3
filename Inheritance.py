#Section INHERITANCE
#Task1
class Student(Person):
    pass
#Task2
class Person:
    def __init__(self, fname):
        self.firstname = fname

    def printname(self):
        print(self.firstname)


class Student(Person):
    pass
x = Student("Mike")
x.printname()