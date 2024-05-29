import random

num = random.randint(0, 20)
print("The number is between 0 and 20")
guess = int(input("Your guess: "))

# while loop
while guess != num:
    print("Try again.")
    guess = int(input("Your guess: "))

# if statement
if guess == num:
    print("YAY! "+str(num)+" was the answer!! :)")