# class Student:
#     def __init__(self, name, rollNo):
#         self.name = name
#         self.rollNo = rollNo
        
#     def printStudent(self):
#         print("My name is", self.name, "and my roll Number is ", self.rollNo)
        
# s1 = Student("Akash", 12)
# s1.printStudent()
# Student.printStudent(s1)

print("Fraction Class")

class Fraction():
    def __init__(self, num = 0, den = 1):
        self.num = num
        self.den = den

f = Fraction(5,8)
print(f.__dict__)
