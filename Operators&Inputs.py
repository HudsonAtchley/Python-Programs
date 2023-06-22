print("Hello, what is your name?")
name = input()
print("Hello,",name)

"""
--------Operators--------
  +
  -
  *
  /
"""
num1 = 45
num2 = 4
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

"""
A few more operators:
exponents - **

integer division - //

ex.
64 / 10 = 6.4
64 // 10 = 6

modulus operator - %

ex.
5 % 2 = 1
"""
num3 = num1 ** num2
num4 = num1 // num2
num5 = num1 % num2
print(num3)
print(num4)
print(num5)

print("Pick a number: ")
num6 = input()
print("Pick another number: ")
num7 = input()

Total = int (num6) + int (num7)
print("The total is:",Total)
