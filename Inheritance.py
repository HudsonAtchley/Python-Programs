# Dog is the parent class
class Dog(object):
    def __init__(self, name, age): # constructor method
        self.name = name
        self.age = age
    
    def introduction(self):
        print("Hello, my name is", self.name,"and I am", self.age,"years old. Nice to meet you!")
        
    def talk(self):
        print("Bark!")
    

class Cat(Dog): # (Dog) means parent, Cat is going to inherit from Dog, Cat is the child class
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
        
    def talk(self):                 # Overriding talk method from above, instead of a bark, replacing with a meow
        print("Meow!")
    
    
alani = Cat("Alani", 7, "Orange")
jasper = Cat("Jasper", 2, "Black")

alani.introduction()
jasper.introduction()

alani.talk()
jasper.talk()



# another example

class Vehicle():
    def __init__(self, price, gas, color):
        self.price = price
        self.gas = gas
        self.color = color
    
    def fillUpTank(self):
        self.gas = 100
        
    def emptyTank(self):
        self.gas = 0
        
    def gasLeft(self):
        return self.gas
    

class Car(Vehicle):
    def __init__(self, price, gas, color, speed):
        super().__init__(price, gas, color)
        self.speed = speed
        
    def beep(self):
        print("Beep beep")
        
        
class Truck(Vehicle):
    def __init__(self, price, gas, color, tires):
        super().__init__(price, gas, color)
        self.tires = tires
    
    def truckBeep(self):
        print("Honk honk")