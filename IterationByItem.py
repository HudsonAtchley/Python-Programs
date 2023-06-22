"""
for loop we did before:

for x in range(0, 10):
    print(x)
"""

fruits = ["apples", "pears", "strawberrys", 3, 8, 90]

# for fruit in fruits:
    # print(fruit)

"""
for fruit in fruits:
    if fruit == "pears":
        print(fruit)
    else:
        print("Not pears")
"""


for x in range(len(fruits)):
    if fruits[x] == "pears":
        print(fruits[x])
    else:
        print("Not a pear")

