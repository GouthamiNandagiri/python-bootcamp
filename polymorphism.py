#polymorphism:
'''-------------------------
Human being:
    in college student
    in theater audience
    in market customer
    in sports players
    in home child
    
--------------------------'''



'''runtime-methodoverriding
compile time-methodoverloading(python doesnot support)
-----------------------------------'''

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f'{self.name},{self.age}'
class Student(Person):
    def __init__(self,name,age,roll,branch):
        super().__init__(name,age)
        self.roll=roll
        self.branch=branch
    def __str__(self):
        perdetails=super().__str__()
        return f'{perdetails},{self.roll},{self.branch}'

class Annualday(Student):
    def __init__(self,name,age,roll,branch,program):
        super().__init__(name,age,roll,branch)
        self.program=program
    def __str__(self):
        studetails=super().__str__()
        return f'{studetails},{self.program}'
aobj=Annualday('john',20,'68','cse','solo')
print(aobj)
