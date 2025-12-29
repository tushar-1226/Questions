class Student():
    def __init__(self, name, rollNo):
        self.name = name
        self.rollNo = rollNo
        
s1 = Student("rohan", 12)
print(s1.__dict__)

s2 = Student("Machli", 33)
print(s2.__dict__)