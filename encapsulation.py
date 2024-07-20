#ENCAPSULATION
''''
binding data and methods into single componentis called Encapsulation
Example:
    class is the best example of encapsulation
#advantages:
    1.code integration:
        security
    2.Access modifiers:
        public,private,protected

'''
class Employee:
    def __init__(self,name,role,salary):
        self.name=name
        self.role=role
        self.__salary=salary #private data
    def get_salary(self):#public method with private data
        return self.__salary
    def Empdisplay(self):#public method
        print(self.name,self.role)
class Company(Employee):
    def __init__(self,cname,loc):
        self.cname=cname
        self.loc=loc
    def Condisplay(self):
        print(self.cname,self.loc)
    def _hiring(self):#protected method
        print("hiring for the manager Role")
cobj=Company('wipro','Gachibowli')
eobj=Employee('Umer','dev',85000)
eobj.Empdisplay()
print(cobj._hiring())
        
