def addTwo(x):
    return (x + 2)**2

def subtractTwo(number):
    return number - 2

def printString(string):
    print(string)

def accel(force, mass):
    a = force / mass
    return a

def doSomething():
    print("Hi")

newNumber = addTwo(12)
print(newNumber)

anotherNumber = subtractTwo(7)
print(anotherNumber)

printString("Hello")
printString("My name is Hudson")
print(accel(2,5))
doSomething()