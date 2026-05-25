class Person:
    def __init__(self,name,age):

        if age<0:
            raise ValueError("Age can not be negative!!")
        self.name=name
        self.age=age

    def show_info(self):
        print(f"Name: {self.name}\nAge: {self.age}")
    
class Student(Person):
    def __init__(self,name,age,roll_no):
        super().__init__(name,age)
        self.roll_no=roll_no
    def show_info(self):
        super().show_info()
        print(f"Roll No: {self.roll_no}")

class Teacher(Person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject=subject
    
    def show_info(self):
        super().show_info()
        print(f"Subject: {self.subject}")

class Principal(Teacher):
    def __init__(self,name,age,subject,exp_years):
        super().__init__(name,age,subject)
        if exp_years<0:
            raise ValueError("Experience can not be negative")
        self.exp_years=exp_years
    def show_info(self):
        super().show_info()
        print(f"Experince: {self.exp_years}")
people=[]
try:
    std=Student("Steni",8,169)
    people.append(std)
except ValueError as e:
    print(e)

try:
    tech=Teacher("Meow",30,"meowmeow")
    people.append(tech)
except ValueError as e:
    print(e)


try:
    prin=Principal("Meowmeow",65,"meow",40)

    people.append(prin)
except ValueError as e:
    print(e)


for p in people:
    p.show_info()
