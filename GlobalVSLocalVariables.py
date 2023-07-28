# global = everywhere, can be used in anything
# local = specific to a certain block of code or to a certain class

var = 9
loop = True


def func(x):
    newVar = 7
    print(newVar)
    if x == 5:
        return newVar

func(2)
# newVar is a local variable to the function, func

def otherFunc():
    newVar = 5
    print(newVar)

otherFunc()

# Global variables
# var and loop would be global variables

def func2(xy):
    newVar2 = 7
    print(var)
    print(loop)
    if xy == 5:
        return newVar2

func2(2)
# prints the var and loop, which is equal to 9 and True