#abstraction;hiddinginteranl details
#abstract-it doesnot body
#non abstract- other name concrete method
'''
from abc import ABC
class RBIBANK(ABC):
    def interest(self):
        pass #abstract method
    def loan(self):
        print("Provides Home loan") #concrete method
class HDFC(RBIBANK):
    def interest(self):
        print("7% interest")
class SBI(RBIBANK):
    def interest(self):
        print("9% interest")
class AXIS(RBIBANK):
    def interest(self):
        print("11% interest")
h1=HDFC()
h1.loan()
h1.interest()
s1=SBI()
s1.loan()
s1.interest()
a1=AXIS()
a1.loan()
a1.interest()
'''
from abc import ABC
class Vehicle(ABC):
    def speed(self):
        pass
    def milage(self):
        pass
    def model(self):
        pass
    def breaks(self):
        print('stop the vehicle')
class Fortuner(Vehicle):
    def speed(self):
        print(' 380 max speed')
    def milage(self):
        print('121kmph')
    def model(self):
        print("new model")
class Rangerover(Vehicle):
    def speed(self):
        print(' 500 max speed')
    def milage(self):
        print('127kmph')
    def model(self):
        print("newcmodel")
f1=Fortuner()
f1.milage()
f1.speed()
f1.model()
f1.breaks()
r1=Rangerover()
r1.milage()
r1.speed()
r1.model()
r1.breaks()



        
        
        
