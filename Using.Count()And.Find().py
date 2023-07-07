# .find(), .count()

string = "hello"
print(string.find("l"))
# gives the value of the specified letter
# -1 = does not find inside string
# for example print(string.find("l") will print 2)

print(string.count("l"))
# counts how many l's are in the string


stringTwo = input("Please type something: ")
if stringTwo.count("_") > 0:
    print("Access Denied.")
else:
    print("Access Granted.")