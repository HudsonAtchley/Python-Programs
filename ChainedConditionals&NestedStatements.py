# and 
# or 
# not

x = 2
y = 3
x == y # False

# for and, both conditions must be true on either side, in order to run.
# This will not print anything, as x, which equals 2, is not equal to y, which is equals 3.
if x == y and x + y == 5:
    print("It runs.")

# This will be true because y is equal to 3, and then x + y is also equal to 5.
if y == 3 and x + y == 5:
    print("It runs.")

# or statement
if y == x or x + y == 5:
    print("It runs, yayayayay")

# not statement
if not (y == x or x + y == 5):
    print("It does run.")
else:
    print(":(")

# not statement, but does run
if not (y == x or x + y == 6):
    print("It does run.")
else:
    print(":(")

# Nested Statements
if x == 2:
    if y == 3:
        print("x = 2, y = 3")
    else:
        print("x = 2, y != 3")
else:
    print("x != 2")

if x == 2:
    if y == 4:
        print("x = 2, y = 3")
    else:
        print("x = 2, y != 3")
else:
    print("x != 2")

if x == 4:
    if y == 4:
        print("x = 2, y = 3")
    else:
        print("x = 2, y != 3")
else:
    print("x != 2")