'''
OOPS:(OBJECT ORIENTED PROGRAMMING)
Real time problems can be solved by using oops
CLASS
OBJECT
CONSTRUCTOR
ABSTRACTION
ENCAPSULATION
INHERITANCE
POLYMORPHISM
---------------------------------------------------------
CLASS:STRUCTURE OF OBJECT OR LOGICAL ENTITY OR class is blueprint of object
creation:(classname first letter should caps)

 class contains func,const,data
 
 syntax:class Class_name:
class Student:
---------------------------------------------------------
OBJECT:PROPERTIES,BEHAVIOUR,IDENTITY

->object is realworld entity
->OBJECT IS THE INSTANCE OF CLASS(COPY)
->INSTANCE IS SUBPART
->OBJECT CONTAINS PROPERTIES,BEHAVIOUR,IDENTITY
------------------------------------------------------------
CONSTRUCTOR:
->IT IS A SPECIAL METHOD OR FUNCTION WHICH IS USED TO INVOKED INSTANCE VARIABLE(obj varaiable)
C->CONSTRUCTOR DOESNOTRETURN ANY VALUE

WHILE CREATING THE OBJECT CONSTRUCTOR WILL CALL IMPLICITLY
there are three types of constructors
1.default
2.parameterised
3.notparameterized
----------------------------------------------------------------
'''
'''
class Student:
    def __init__(self,name,roll,branch,address,email):
        self.name=name
        self.roll=roll
        self.branch=branch
        self.address=address
        self.email=email
    def display(self):
        print("Name is:",self.name)
        print("roll is:",self.roll)
        print("branch is:",self.branch)
        print("address is:",self.address)
        print("email is:",self.email)
s1=Student('Gouthami',501,'CSE','Hyderabad','gouthaminandagiri@gmail.com')
s1.display()
'''



'''
class Employee:
    def __init__(self,ename,eid,email,address,position):
        self.ename=ename
        self.eid=eid
        self.email=email
        self.address=address
        self.position=position
    def display(self):
        print("Name is:",self.ename)
        print("id is:",self.eid)
        print("email is:",self.email)
        print("address is:",self.address)
        print("position is:",self.position)
e1=Employee('Gouthami',502,'gouthaminan@gmail.com','hyderabad','team manager')
e1.display()
'''

'''
static
1.static is used for memory management
2.Instead of creating individually a common data create a static data and pass the copy to all the objects
'''
'''
class Student:
    #static data
    branch='CSE'
    def __init__(self,name,roll,address,email):
        self.name=name
        self.roll=roll
        self.address=address
        self.email=email
    def display(self):
        print("Name is:",self.name)
        print("roll is:",self.roll)
        print("branch is:",Student.branch)
        print("address is:",self.address)
        print("email is:",self.email)
s1=Student('Gouthami',501,'CSE','Hyderabad','gouthaminandagiri@gmail.com')
s1.display()
'''

'''
  Without creating display function
  
class Student:
    #static data
    branch='CSE'
    def __init__(self,name,roll,address,email):
        self.name=name
        self.roll=roll
        self.address=address
        self.email=email
    def __str__(self):
        return f'{self.name} {self.roll} {self.roll}  {Student.branch}  {self.email}'
s1=Student('srivani',101,'HYd','srivani@gmail.com')
s2=Student('gouthami',102,'knr','gouthaminan@gmail.com')       
print(s1)
print(s2)
'''


        
        
