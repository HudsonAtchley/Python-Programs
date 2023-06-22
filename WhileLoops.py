"""
while condition == True:
     do this
     break
"""
loop = True

while loop:
    password = input("Insert your password ")
    if password == "stop":
        loop = False
        break
