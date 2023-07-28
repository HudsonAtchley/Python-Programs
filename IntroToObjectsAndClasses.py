x = 5
y = "string"
f = 5.5
print(type(x)) # <class 'int'>
print(type(y)) # <class 'str'>

print(y.upper()) # upper isn't a function, it is a method
# print(x.upper()) is not going to work, due to the fact that x is an object of type int
# print(f.upper()) is also not going to work, due to the fact that f is an object of type float

def func(x):
    return x + 1

print(func(5))

# class is what you call with the dot operator
