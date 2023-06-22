# If
# elif
# else

""" 
if condition === True:
    do this
"""

"""
age = input("Input your age: ")

if int(age) == 16:
    print("Hey, you're 16.")
    
age2 = input("Input your age: ")

if int(age2) > 16:
    print("Hey, you're older than 16.")
"""

"""
age3 = input("Input your age: ")

if int(age3) >= 16:
    print("Hey, you're 16 or older.")
else:
    print("Hey, you're younger than 16.")
"""

height = input("Enter your height, in meters: ")

if int(height) < 1:
    print("You are not tall enough to ride, under 1 meter.")
elif int(height) == 5:
    print("Wow, you are tall.")
elif int(height) > 2:
    print("You are not tall enough to ride, over 2 meters.")
else:
    print("You may ride.")

