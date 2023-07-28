class Dog(object):
    def __init__(self, name, age, sex): # constructor method
        self.name = name
        self.age = age
        self.sex = sex
        #print("Nice you made a dog!")
    
    def introduction(self):
        print("Hello, my name is", self.name,"and I am a",self.sex,"and I am", self.age,"years old. Nice to meet you!")
    
    def change_age(self, age):
        self.age = age
    
    def add_weight(self, weight):
        self.weight = weight

zeke = Dog("Zeke", 6, "boy",)
rosie = Dog("Rosie", 2, "girl")
rex = Dog("Rex", 6, "boy")

rosie.change_age(1)
zeke.introduction()
rosie.introduction()
rex.introduction()
zeke.add_weight(23)

print(zeke.age)
print(zeke.age)
print(zeke.sex)
print(zeke.weight)
