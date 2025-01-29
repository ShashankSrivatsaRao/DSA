#Classes are blueprints of properties and methods
#objects are the instances of classes
# __init__ is a constructor
#self is a reference to the object of the same class
"""
class office:
        def __init__(self,name,domain):
            self.name=name
            self .domain=domain
        
        def does_work(self):
            if self.domain == 'IT':
                print(self.domain,' Sector')
            elif self.domain =='Consulting':
                print(self.domain,' Sector')
        def stocks(self):

            print('Stocks of ',self.name)


Subhanu =office('Subhanu','Consulting')
Subhanu.does_work()
Subhanu.stocks()

Rapidd=office('Rapidd','IT')
Rapidd.does_work()
Rapidd.stocks()
"""

#Inheritance
#Inheritance is a way of creating a new class for using details of an existing class without modifying it.
#The newly formed class is a derived class (or child class).
#Hierarchichal Inheritance
""""
class Box:
    def purpose(self):
        print('To hold things')
    
class LunchBox(Box):
    def __init__(self):
        self.size = 'small'
    
    def purpose(self):
        print('To hold lunch')
class ElectronicBox(Box):
    def __init__(self):
        self.size = 'big'
    
    def purpose(self):
        super().purpose()   #super() is used to call the parent class method
        print('To hold Electronic items')

A=LunchBox()
A.purpose()
B=ElectronicBox()   
B.purpose()    
"""
#Multiple Inheritance
class Mother:
    def cooking(self):
        print('Mother cooks paneer')
class Father:
    def working(self):
        print("Father works")
class children(Father,Mother):
    def __init__(self,name):
        self.name=name
    def sports(self):
        print(self.name,' plays cricket')  

Shashank =children('Shashank')
Shashank.sports()
Shashank.cooking()
Shashank.working()  

